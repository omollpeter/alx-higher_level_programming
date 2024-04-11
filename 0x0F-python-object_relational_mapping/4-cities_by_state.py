#!/usr/bin/python3
"""
This module is a script that lists all cities from the database
hbtn_0e_4_usa
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
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities" +
        " LEFT JOIN states" +
        " ON cities.state_id = states.id" +
        " ORDER BY cities.id ASC"
    )
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
