"""
Name: Database Loader Script
Author: Maheshkrishna A G
Description: The script access the task_data.csv file and read them to load into PYTHON_TEST.TASK_DATA table.
Database: MySQL 8.0.16 in AWS RDS
Date: 19-Jan-2020
"""

import pandas as pd
import mysql.connector as mysql
import time

df = pd.read_csv("PATH TO task_data.csv")

# Initiate DB Connection
db = mysql.connect(host="python-db.cxxjqwuxxbfj.eu-west-1.rds.amazonaws.com", user="user_one",
                   passwd=base64.b64decode(b'TWFzdGVyIzEyMw=='.decode("utf-8")).decode("utf-8"),
                   db="python_test")
cur = db.cursor()

# Traverse through each data frame to create a record in the PYTHON_TEST.TASK_DATA table
for i in df.index:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(str(df['timestamp'][i]), "%m/%d/%Y %H:%M:%S"))
    try:
        cur.execute("INSERT INTO TASK_DATA VALUES (%s,%s,%s,%s)", (int(df['id'][i]), str(timestamp),
                                                                   float(df['temperature'][i]), str(df['duration'][i])))
    except Exception as e:
        print(e)
    db.commit()

db.close()
