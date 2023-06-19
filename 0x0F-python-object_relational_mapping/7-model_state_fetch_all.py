#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get the MySQL connection information from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the connection string
    connection_string = "mysql+mysqldb://" + username + ":" + password + \
        "@localhost:3306/" + database

    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)

    # Bind the engine to the base class
    Base.metadata.bind = engine

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Retrieve all State objects and sort them by ID in ascending order
    states = session.query(State).order_by(State.id).all()

    # Display the State objects
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
