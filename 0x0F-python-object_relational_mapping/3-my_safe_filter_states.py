#!/usr/bin/python3
"""
Script to list all states from the database `hbtn_0e_0_usa` that start with 'N'
"""

import MySQLdb
import sys


def main(username, password, db_name=sys.argv[1], sys.argv[2], sys.argv[3]):

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

    query = """
		SELECT *
		FROM state
		WHERE BINARY name=%s
		ORDER BY state.id ASC
"""
    cursor.execute(query, (serch_param))

    rows = cusor.fetchall()

    for row in rows:
        print(row)

        cursor.close()
        db.close()

        if __name__ == "__main__":
		argv = sys.argv
		main(argv[1], argv[2], argv[3], argv[4])
