#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument
from the database
"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    srch_name = sys.argv[4]
    state = session.query(State).filter(State.name == srch_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
