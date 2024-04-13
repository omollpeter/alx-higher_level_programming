#!/usr/bin/python3
"""
This script lists all city objects from the database along with their
states

"""


import sys
from relationship_city import City, Base
from relationship_state import State
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

    cities = session.query(City).order_by(City.id.asc()).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
