#!/usr/bin/python3
"""
Module: 5-filter_cities
Description: List states associated with a city.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    List all states associated with a city.
    """
    arguments = sys.argv
    user_ = arguments[1]
    passwd_ = arguments[2]
    database = arguments[3]
    name_ = arguments[-1]
    db = MySQLdb.connect(
        host="localhost", user=user_, passwd=passwd_, db=database)
    cur = db.cursor()
    cur.execute("""
            SELECT cities.id, cities.name
            FROM cities
            JOIN states
            ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %(name)s
            ORDER BY cities.id ASC
        """, {'name': name_})
    rows = cur.fetchall()
    if rows is not None:
        string = ", ".join([r[1] for r in rows])
        print(string)
