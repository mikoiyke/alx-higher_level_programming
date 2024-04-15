#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    argv = sys.argv

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    cur = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id
    """

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
