#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
with their states
"""


import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
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

    cities = session.query(City.id, City.name, State.name.label("state_name")
                           ).join(State).order_by(City.id.asc()).all()

    for city in cities:
        print(f"{city.state_name}: ({city.id}) {city.name}")

    session.close()
