#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of the database `hbtn_0e_0_usa`
where name matches the argument exactly.
"""
import MySQLdb
import sys


def main():
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Establish a database connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Prepare SQL query string
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"

    # Execute the SQL query
    cur.execute(query, (state_name,))

    # Fetch all results
    states = cur.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close cursor and connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
