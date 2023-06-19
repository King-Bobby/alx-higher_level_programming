#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Assign the argument name to a variable
    n_arg = sys.argv[4]

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (n_arg,))
    # Fetch all the rows from the result set
    results = cursor.fetchall()

    # Iterate over the rows and display the state information
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
