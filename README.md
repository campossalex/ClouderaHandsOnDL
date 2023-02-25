# Cloudera Tech Day 1, End to End Data Lifecycle

This document describes the process to setup the labs for Cloudera Tech Day 1, End to End Data Lifecycle

## Enviroment:

Setup a CDP PC environment, with following services:

- Data Hub, Streams Messaging Light Duty: it will be used to publish and consume the main data source for the use case
- CDF: consume data from Kafka topic and stoore and Iceberg table
- CDE: data preparation
- CDW: data exploration and build reports
- CML: traing a ML model to score customer churn

