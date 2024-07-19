#!/usr/bin/python3
"""
Module: 0-select_states
Description: Manipulating databases using MySQLdb
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    List all states in the database in ASC order.
    """
    arguments = sys.argv
    user_ = arguments[1]
    passwd_ = arguments[2]
    database = arguments[-1]
    db = MySQLdb.connect(
        host="localhost", user=user_, passwd=passwd_, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for r in rows:
        print(r)
