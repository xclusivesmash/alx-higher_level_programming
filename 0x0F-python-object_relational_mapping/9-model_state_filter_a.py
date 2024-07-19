#!/usr/bin/python3
"""
Module: 9-model_state_filter_a
Description: List state objects from a database.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    list all State objects from the database
    hbtn_0e_6_usa
    """
    username_ = argv[1]
    passwd_ = argv[2]
    db = argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(username_, passwd_, db), pool_pre_ping=True)
    # start session
    Session = sessionmaker(bind=engine)
    session = Session()
    Q = session.query(State).filter(State.name.contains("a"))
    Q = Q.order_by(State.id)

    if Q:
        for r in Q:
            string = "{}: {}".format(r.id, r.name)
            print(string)
