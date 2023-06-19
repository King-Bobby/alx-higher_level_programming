#!/usr/bin/env python3
"""
Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Assign values to variables
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the connection string
    connection_string = f"mysql+mysqldb://" + username + ":" + \
        password + "@localhost:3306/" + database

    # Create the engine
    engine = create_engine(connection_string)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State objects containing the letter 'a'
    query = session.query(State)
    states = query.filter(State.name.like('%a%')).order_by(State.id).all()

    if not states:
        print("Nothing")
    else:
        for state in states:
            print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
