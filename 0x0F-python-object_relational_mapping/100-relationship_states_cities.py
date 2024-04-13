#!/usr/bin/python3
"""
This script creates the state "California" with a city "San Franscisco"
in a database

"""


import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    calif_state = State(name="California")
    san_city = City(name="San Francisco", state=calif_state)

    session.add_all([calif_state, san_city])
    session.commit()

    session.close()
