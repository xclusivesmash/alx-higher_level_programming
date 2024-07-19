#!/usr/bin/python3
"""
Module: 2-my_filter_states
Description: List states where input matches name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    List all states in the database in ASC order.
    The input must match name parameter.
    """
    arguments = sys.argv
    user_ = arguments[1]
    passwd_ = arguments[2]
    database = arguments[3]
    name_ = arguments[-1]
    db = MySQLdb.connect(
        host="localhost", user=user_, passwd=passwd_, db=database)
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC".format(name_))
    rows = cur.fetchall()
    for r in rows:
        print(r)
