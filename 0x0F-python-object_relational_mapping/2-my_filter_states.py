#!/usr/bin/python3
"""
Script to list all states from the database `hbtn_0e_0_usa` that match a name
"""

import MySQLdb
import sys

def main():
    if len(sys.argv) != 5:
        print("Usage: ./script.py username password database_name state_name")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8")

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # SQL query to fetch states that match the given name, sorted by 'id'
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch all the results
    states = cur.fetchall()

    # Print each state from the results
    for state in states:
        print(state)

    # Close the cursor and the connection
    cur.close()
    db.close()

if __name__ == '__main__':
    main()
