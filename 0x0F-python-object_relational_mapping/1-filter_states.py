#!/usr/bin/python3
"""
return states starting with 'N'
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL; filter names starting with 'N'
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
