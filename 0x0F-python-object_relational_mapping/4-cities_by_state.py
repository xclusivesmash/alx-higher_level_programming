#!/usr/bin/python3
"""
Module: 4-cities_by_state
Description: List cities from a given database.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    List all cities in the database in ASC order.
    """
    arguments = sys.argv
    user_ = arguments[1]
    passwd_ = arguments[2]
    database = arguments[3]
    db = MySQLdb.connect(
        host="localhost", user=user_, passwd=passwd_, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for r in rows:
        print(r)
