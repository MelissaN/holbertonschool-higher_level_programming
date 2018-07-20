#!/usr/bin/python3
"""
return cities that are in the state given (tables 'cities' 'states)
parameters given to script: username, password, database, state
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

    # create cursor to exec queries using SQL; join two tables for all info
    cursor = db.cursor()
    sql_cmd = """SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC"""
    cursor.execute(sql_cmd, (argv[4], ))

    # format the printing of cities of same state separated by commas
    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))

    cursor.close()
    db.close()
