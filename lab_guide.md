# Lab Guide

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
STORED AS PARQUET
```




### 3. For DataViz...
```

1.- Clonar los numéricos, renombrar las string antiguas y los clones pasarlos a measure
2.- para monthlycharges y totalcharges usar regexp_replace([monthlycharges_str], ',', '.') y regexp_replace([totaalcharges_str], ',', '.')

En SQL

DESCRIBE HISTORY user001.telco_data_curated
SELECT * FROM user001.telco_data_curated FOR SYSTEM_VERSION AS OF snapshotid


Para el modelo, crear una dimensión llamada result con la siguiente expresión
cviz_rest('{"url":"https://modelservice.ml-2f3fd21b-2f8.spain-ho.z20f-vg26.cloudera.site/model","accessKey":"m8nx69lkokd92bq27pli2u1fzz7j5i4x","colnames":["monthlycharges","totalcharges","tenure","gender","dependents","onlinesecurity","multiplelines","internetservice","seniorcitizen","techsupport", "contract","streamingmovies", "deviceprotection", "paymentmethod","streamingtv","phoneservice", "paperlessbilling","partner", "onlinebackup"],"response_colname":"result"}')

```
