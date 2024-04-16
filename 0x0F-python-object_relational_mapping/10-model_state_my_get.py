#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main(username, password, dbname, search):
    db_u = f"""mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"""
    engine = create_engine(db_u)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == argv[4]).first()

    if (states):
        print(f"{states.name}")
    else:
        print('Not found')

    session.close()


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3], argv[4])
