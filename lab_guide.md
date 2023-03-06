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
