#!/usr/bin/python3
"""
a script that lists all City objects from the database hbtn_0e_101_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == '__main__':
    # Get the MySQL credentials and database name from command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the connection engine
    connection_string = f"mysql+mysqldb://" + username + ":" \
        + password + "@localhost:3306/" + database
    engine = create_engine(connection_string)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Retrieve all City objects and their associated State objects
    cities = session.query(City).join(State).order_by(City.id).all()

    # Iterate over the cities and print the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()
