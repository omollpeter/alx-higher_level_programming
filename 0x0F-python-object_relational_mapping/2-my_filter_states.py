#!/usr/bin/python3
"""
This module is a script that lists all states where name matches search
argument from the database hbtn_0e_0_usa
It uses MySQLdb module/interface to connect to the database and
execute the queries
The script takes 4 arguments - mysql username, mysql password
database name, 
"""


import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    table = "states"
    srch_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM {table}" +
        f" WHERE BINARY name = '{srch_name}' ORDER BY id ASC"
    )
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
