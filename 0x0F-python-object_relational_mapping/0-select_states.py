#!/usr/bin/python3
"""
This module is a script that lists all states from the database
hbtn_0e_0_usa
It uses MySQLdb module/interface to connect to the database and
execute the queries
The script takes three arguments - mysql username, mysql password
and database name
"""


import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    table = "states"

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {table} ORDER BY id ASC")
    data = cursor.fetchall()

    for row in data:
        print(row)
    
    cursor.close()
    db.close()
