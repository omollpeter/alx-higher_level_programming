#!/usr/bin/python3
"""
This script lists all state objects that contain the letter a from the
database hbtn_0e_6_usa
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

    st_with_a = session.query(State).filter(State.name.like("%a%")).order_by(
        State.id.asc()
    ).all()

    for state in st_with_a:
        print(f"{state.id}: {state.name}")
