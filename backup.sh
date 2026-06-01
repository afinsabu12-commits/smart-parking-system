#!/bin/bash

DATE=$(date +%F-%H-%M)

mysqldump -u root -pafin@123 smartparking > backup-$DATE.sql

aws s3 cp backup-$DATE.sql s3://smart-parking-afin/

rm backup-$DATE.sql
