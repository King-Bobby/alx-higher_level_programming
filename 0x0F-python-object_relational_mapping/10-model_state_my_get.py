#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Assign values to variables
    username, password, = sys.argv[1], sys.argv[2]
    database, state_name = sys.argv[3], sys.argv[4]

    # Create the connection string
    connection_string = f"mysql+mysqldb://" + username + ":" + \
        password + "@localhost:3306/" + database

    # Create the engine
    engine = create_engine(connection_string)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()
