#!/usr/bin/python3
"""
Script to list all states from the database `hbtn_0e_0_usa` that start with 'N'
"""

import MySQLdb
import sys


def main(username, password, db_name, search_param):

	db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8")

    cur = db.cursor()

    query = """
                SELECT *
                FROM states
                WHERE BINARY name LIKE %s
                ORDER BY id ASC
            """
    cur.execute(query, (search_param + '%',))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: ./script.py username password db_name search_param")
