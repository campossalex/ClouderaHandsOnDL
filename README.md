# Cloudera Hands-on Experience, Data Lifecycle

## Environment Access:

Please connect to Lab Environment

Environment URL:      

Username:          user001 - user050  
Access Password:     

## Lab Guide

Some cool stuff we will do today:

Portuguese manuals:

CDF lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/portuguese/CDP-PC-CDF.pdf  
CDE lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/portuguese/CDP-PC-CDE.pdf  
CDW lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/portuguese/CDP-PC-CDW.pdf  
CML lab: https://github.com/campossalex/ClouderaHandsOn/blob/main/lab_guides_pdf/portuguese/CDP-PC-CML.pdf  

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
cviz_rest('{"url":"<workspace_url>","accessKey":"<access_key>","colnames":["monthlycharges","totalcharges","tenure","gender","dependents","onlinesecurity","multiplelines","internetservice","seniorcitizen","techsupport", "contract","streamingmovies", "deviceprotection", "paymentmethod","streamingtv","phoneservice", "paperlessbilling","partner", "onlinebackup"],"response_colname":"result"}')

## Iceberg Time Tavel
List table snapshosts:  
``` 
DESCRIBE HISTORY <user_id>.telco_data_curated

``` 
Query table with a specific snapshot id:  
``` 
SELECT * FROM user001.telco_data_curated FOR SYSTEM_VERSION AS OF snapshotid

``` 

