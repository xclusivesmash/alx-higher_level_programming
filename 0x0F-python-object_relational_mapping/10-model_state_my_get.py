#!/usr/bin/python3
"""
Module: 10-model_state_my_get
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
    name_ = argv[4]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(username_, passwd_, db), pool_pre_ping=True)
    # start session
    Session = sessionmaker(bind=engine)
    session = Session()
    # start query
    Q = session.query(State).filter(State.name == name_).first()

    if Q:
        print("{}".format(Q.id))
    else:
        print("Not found")
