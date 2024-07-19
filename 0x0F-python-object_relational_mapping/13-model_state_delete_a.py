#!/usr/bin/python3
"""
Module: 13-model_state_delete_a
Description: Delete state objects from a
database named hbtn_0e_6_usa.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Delete State objects from the database
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
    # start session
    session = Session()

    # start of work
    Q = session.query(State).filter(State.name.contains("a"))
    if Q:
        for r in Q:
            session.delete(r)
    session.commit()
    # end of work

    # close session
    session.close()
