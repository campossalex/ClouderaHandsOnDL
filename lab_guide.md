# Lab Guide Setup

### 0. Permission in Renger  

Add the user group to following policies:  

Hadoop SQL:  
all - database, table, column  
all - storage-type, storage-url  

Kafka (cluster name):  
all - consumergroup  
all - topic  

### 1. Create Iceberg table statement

```
CREATE EXTERNAL TABLE ${user_database}.telco_iceberg_kafka(
`multiplelines` string,
`paperlessbilling` string,
`gender` string,
`onlinesecurity` string,
`internetservice` string,
`techsupport` string,
`contract` string,
`churn` string,
`seniorcitizen` string,
`deviceprotection` string,
`streamingtv` string,
`streamingmovies` string,
`totalcharges` string,
`partner` string,
`monthlycharges` string,
`customerid` string,
`dependents` string,
`onlinebackup` string,
`phoneservice` string,
`tenure` string,
`paymentmethod` string)
ROW FORMAT SERDE
'org.apache.iceberg.mr.hive.HiveIcebergSerDe'
STORED BY
'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler'

```

### 2. Create Iceberg curated table - Parquet format
```
CREATE EXTERNAL TABLE ${user_database}.telco_data_curated(
`multiplelines` string,
`paperlessbilling` string,
`gender` string,
`onlinesecurity` string,
`internetservice` string,
`techsupport` string,
`contract` string,
`churn` string,
`seniorcitizen` string,
`deviceprotection` string,
`streamingtv` string,
`streamingmovies` string,
`totalcharges` float,
`partner` string,
`monthlycharges` float,
`customerid` string,
`dependents` string,
`onlinebackup` string,
`phoneservice` string,
`tenure` float,
`paymentmethod` string)
ROW FORMAT SERDE
'org.apache.iceberg.mr.hive.HiveIcebergSerDe'
STORED BY
'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler' 
STORED AS PARQUET
```

### 3. Create master tables:

```
CREATE DATABASE master_data;

CREATE TABLE master_data.contract (id STRING, description STRING) STORED BY 'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler' STORED AS PARQUET;
INSERT INTO master_data.contract
values('1', 'Month-to-month'),
('2', 'One year'),
('3', 'Two year');

CREATE TABLE master_data.misc (id STRING, description STRING) STORED BY 'org.apache.iceberg.mr.hive.HiveIcebergStorageHandler' STORED AS PARQUET;
INSERT INTO master_data.misc 
values('Y', 'Yes'),
('N', 'No'),
('F', 'Female'),
('M', 'Male'),
('1', 'Yes'), 
('0', 'No');
```

### 4. For DataViz...
```

1.- Clone numeric variables, rename string and pass clones to measures
2.- for monthlycharges y totalcharges use regexp_replace([monthlycharges_str], ',', '.') and regexp_replace([totaalcharges_str], ',', '.')

In SQL

DESCRIBE HISTORY user001.telco_data_curated
SELECT * FROM user001.telco_data_curated FOR SYSTEM_VERSION AS OF snapshotid


Finally for the model (dimension variable)
cviz_rest('{"url":"https://modelservice.ml-2f3fd21b-2f8.spain-ho.z20f-vg26.cloudera.site/model","accessKey":"m8nx69lkokd92bq27pli2u1fzz7j5i4x","colnames":["monthlycharges","totalcharges","tenure","gender","dependents","onlinesecurity","multiplelines","internetservice","seniorcitizen","techsupport", "contract","streamingmovies", "deviceprotection", "paymentmethod","streamingtv","phoneservice", "paperlessbilling","partner", "onlinebackup"],"response_colname":"result"}')


If trying to aggregate a string variable: avg(cast([monthlycharges] as double))

```

Add the CML Workshop URL to Data Viz -> Site Setting -> Remote Data Settings:  
URL Format example: https://modelservice.ml-369083c3-99e.ssa-hol.yu1t-vbzg.cloudera.site/model

