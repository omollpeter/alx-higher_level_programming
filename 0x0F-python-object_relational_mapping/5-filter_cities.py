#!/usr/bin/python3
"""
This module is a script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa

It uses MySQLdb module/interface to connect to the database and
execute the queries
The script takes 4 arguments - mysql username, mysql password,
database name and search state arg
"""


import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    srch_name = sys.argv[4]
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
        "SELECT cities.name FROM cities" +
        " JOIN states ON cities.state_id = states.id" +
        " WHERE states.name = %s", (srch_name,)
    )
    data = cursor.fetchall()

    cities = []
    for row in data:
        cities.append(row[0])

    if not cities:
        print()
    else:
        for i in range(len(cities)):
            print(cities[i], end="")
            if i == len(cities) - 1:
                print()
                continue
            print(", ", end='')

    cursor.close()
    db.close()
