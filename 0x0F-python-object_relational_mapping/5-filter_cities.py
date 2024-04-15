#!/usr/bin/python3

"""Write a script that takes in the name of a state as an argument and list"""

import MySQLdb
import sys


def o_ore(usr, passwd, db, state):
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=passwd,
        db=db,
        charset="utf8"
    )

    cur = conn.cursor()

    cur.execute(f"""SELECT cities.name FROM cities
            WHERE state_id =
            (SELECT id FROM states
            WHERE name = '{state}')
            ORDER BY cities.id ASC"""
                )

    rows = cur.fetchall()

    flattened_list = [str(tup[0]) for tup in rows]

    comma_separated_values = ", ".join(flattened_list)

    print(comma_separated_values)

    cur.close()
    conn.close()


if __name__ == '__main__':
    arg = sys.argv
    o_ore(arg[1], arg[2], arg[3], arg[4])
