#!/usr/bin/python3
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

    # Get the state name argument
    state_name = sys.argv[4]

    # Prepare the parameterized query
    query = "SELECT cities.name " \
            "FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "WHERE states.name = %s " \
            "ORDER BY cities.id ASC"

    try:
        # Execute the query with the state name as parameter
        cursor.execute(query, (state_name,))

        # Fetch all the rows from the result set
        results = cursor.fetchall()

        # Extract the city names from the results
        cities = [row[0] for row in results]

        # Display the city names
        print(", ".join(cities))

    except MySQLdb.Error as e:
        print("Error executing query:", str(e))

    # Close the cursor and database connection
    cursor.close()
    db.close()
