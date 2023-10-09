import os
from datetime import datetime
import sys
import configparser
from pyspark.sql import SparkSession
from pyspark.sql.types import *
#import pandas as pd

config = configparser.ConfigParser()
config.read('/app/mount/parameters.conf')
data_lake_name=config.get("general","data_lake_name")

spark = SparkSession \
    .builder \
    .appName("ICEBERG LOAD") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog")\
    .config("spark.sql.catalog.spark_catalog.type", "hive")\
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")\
    .config("spark.yarn.access.hadoopFileSystems", data_lake_name)\
    .getOrCreate()

DATABASE=sys.argv[1]
print("Running job as Username: ", DATABASE)

#CREATE EXTERNAL TABLE ext_t1 STORED AS ICEBERG TBLPROPERTIES ('iceberg.table_identifier'='default.telco_iceberg');

from pyspark.sql.functions import rand,abs,when,regexp_replace
print("spark_catalog."+ DATABASE + ".telco_data_curated")
df=spark.read.format("iceberg").load("spark_catalog."+ DATABASE + ".telco_data_curated")

df=df.select('customerid','monthlycharges', 'tenure','churn').where(df.churn != 'Yes')
df=df.drop_duplicates()
df=df.drop_duplicates(['customerid'])
df=df.withColumn("monthlycharges",df.monthlycharges.cast(DoubleType()))
df=df.withColumn("tenure",df.tenure.cast(DoubleType()))

df=df.withColumn("monthlycharges",df["monthlycharges"]+df["monthlycharges"]*(2*rand()-1))
df=df.withColumn("monthlycharges",df.monthlycharges)

spark.sql("drop table if exists " + DATABASE + "modtable")
df.write.mode("overwrite").saveAsTable(DATABASE+"modtable")


spark.sql("MERGE INTO spark_catalog."+ DATABASE + ".telco_data_curated t USING "+DATABASE+"modtable s ON t.customerid = s.customerid WHEN MATCHED THEN UPDATE SET monthlycharges = s.monthlycharges")

spark.sql("drop table if exists " + DATABASE + "modtable")
