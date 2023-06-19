#!/usr/bin/python3
"""
a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    # Retrieve all State objects and their corresponding City objects
    states = session.query(State).order_by(State.id).all()

    # Iterate over the states and print the results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()
