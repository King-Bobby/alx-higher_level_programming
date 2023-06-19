#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa:
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

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the result set
    results = cursor.fetchall()

    # Iterate over the rows and display the state information
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
