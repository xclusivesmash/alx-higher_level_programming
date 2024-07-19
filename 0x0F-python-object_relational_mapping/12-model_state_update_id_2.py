#!/usr/bin/python3
"""
Module: 12-model_state_update_id_2
Description: Change a state objects from a
database named hbtn_0e_6_usa.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Change a State object from the database
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
    Q = session.query(State).filter(State.id == 2).first()
    Q.name = "New Mexico"
    session.commit()
    # end of work

    # close session
    session.close()
