# Write a program for sql connection.

import mysql.connector
from tabulate import tabulate

mysqldb = mysql.connector.connect(
    host="localhost",
    user="hacker07",
    passwd="admin1234",
    db = "test"
)

cursor = mysqldb.cursor()
cursor.execute("SELECT * FROM test.student_master")

rows = cursor.fetchall()
print("\n",tabulate(rows, headers=cursor.column_names),"\n")

    