#!/usr/bin/python3
"""
Script that changes the name of a State object
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Assign values to the variables
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

    # Retrieve the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Check if the State object exists
    if state is None:
        print("Not found")
        sys.exit(0)

    # Change the name of the State
    state.name = "New Mexico"

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
