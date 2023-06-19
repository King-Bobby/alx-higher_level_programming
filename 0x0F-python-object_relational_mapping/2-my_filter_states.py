#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            )
    n_arg = sys.argv[4]
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (n_arg,))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
