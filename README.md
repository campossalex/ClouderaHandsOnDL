# Cloudera Hands-on Experience Madrid, Data Lifecycle

## Enviroment Access:

Please connect to Lab Environment

Enviroment URL:   
https://login.cdpworkshops.cloudera.com/auth/realms/marketing-workshop2/protocol/saml/clients/cdp-sso  

Username:   user001 - user050  
Password:   password

## Lab Guide

Some cool stuff we will do today:

CDF lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/CDP-PC-CDF.pdf  
CDE lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/CDP-PC-CDE.pdf  
CDW lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/CDP-PC-CDW.pdf  

## Configurations:  

### ChurnScore Expression:  
cviz_rest('{"url":"<url_del_workspace>","accessKey":"<access_key>","colnames":["monthlycharges","totalcharges","tenure","gender","dependents","onlinesecurity","multiplelines","internetservice","seniorcitizen","techsupport", "contract","streamingmovies", "deviceprotection", "paymentmethod","streamingtv","phoneservice", "paperlessbilling","partner", "onlinebackup"],"response_colname":"result"}')

## Iceberg Time Tavel
``` 
DESCRIBE HISTORY <user_id>.telco_data_curated
SELECT * FROM user001.telco_data_curated FOR SYSTEM_VERSION AS OF snapshotid

``` 
