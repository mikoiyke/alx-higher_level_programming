#!/usr/bin/python3
"""
Write a script that prints the first State object from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main(username, password, dbname):
    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print('Nothing')

    session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        main(argv[1], argv[2], argv[3])
    else:
        print("Usage: ./script.py username password dbname")
