# Cloudera Hands-on Experience, Data Lifecycle

## Enviroment Access:

Please connect to Lab Environment

Enviroment URL:   
https://login.cdpworkshops.cloudera.com/auth/realms/marketing-workshop2/protocol/saml/clients/cdp-sso  

Username:          user001 - user050  
Access Password:   G0yvxvdms5srhyKF    

## Lab Guide

Some cool stuff we will do today:

English manuals:

CDF lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/english/CDP-PC-CDF.pdf  
CDE lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/english/CDP-PC-CDE.pdf  
CDW lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/english/CDP-PC-CDW.pdf  
CML lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/english/CDP-PC-CML.pdf  

Spanish manuals:

CDF lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/spanish/CDP-PC-CDF.pdf  
CDE lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/spanish/CDP-PC-CDE.pdf  
CDW lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/spanish/CDP-PC-CDW.pdf  
CML lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/spanish/CDP-PC-CML.pdf  

## CML github repo url  
https://github.com/campossalex/TelcoChurn

## Configurations:  

### ChurnScore Expression:  
cviz_rest('{"url":"<url_del_workspace>","accessKey":"<access_key>","colnames":["monthlycharges","totalcharges","tenure","gender","dependents","onlinesecurity","multiplelines","internetservice","seniorcitizen","techsupport", "contract","streamingmovies", "deviceprotection", "paymentmethod","streamingtv","phoneservice", "paperlessbilling","partner", "onlinebackup"],"response_colname":"result"}')

## Iceberg Time Tavel
List table snapshosts:  
``` 
DESCRIBE HISTORY <user_id>.telco_data_curated

``` 
Query table with a specific snapshot id:  
``` 
SELECT * FROM user001.telco_data_curated FOR SYSTEM_VERSION AS OF snapshotid

``` 

