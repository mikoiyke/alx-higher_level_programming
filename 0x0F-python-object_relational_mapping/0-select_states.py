#!/usr/bin/python3
"""Script to list all states from the database `hbtn_0e_0_usa`"""

import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./script.py username password database_name")
        return

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # SQL query to fetch all states sorted by 'id'
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cur.fetchall()

    # Print each state from the results
    for state in states:
        print(state)

    # Close the cursor and the connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
