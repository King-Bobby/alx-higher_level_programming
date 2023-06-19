#!/usr/bin/python3
"""
Script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Assign values to variables
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the connection string
    connection_string = f"mysql+mysqldb://" + username + \
        ":" + password + "@localhost:3306/" + database

    # Create the engine
    engine = create_engine(connection_string)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Retrieve the State objects with names containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the State objects
    for state in states:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
