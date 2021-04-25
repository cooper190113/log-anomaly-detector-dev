#! /bin/sh
# sh ui-shell-script.sh
export CUSTOMER_ID="#1234567"
export SQL_CONNECT="mysql+pymysql://zak:password@localhost/factstore"
nohup python3 app.py --metric-port 8081 ui --port 5001 > nohup.out 2>&1 &