#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        cursor.execute(query, (sys.argv[4],))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("Error executing query:", str(e))

    cursor.close()
    db.close()
