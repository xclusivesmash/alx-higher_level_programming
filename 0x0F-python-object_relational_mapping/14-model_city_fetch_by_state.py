#!/usr/bin/python3
"""
Module: 14-model_city_fetch_by_state
Description: List city objects from a
database named hbtn_0e_6_usa.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    """
    List City objects from the database
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
    Q = session.query(City, State).join(State).order_by(City.id)
    if Q:
        for c, s in Q.all():
            string = "{}: ({}) {}".format(s.name, c.id, c.name)
            print(string)
    session.commit()
    # end of work

    # close session
    session.close()
