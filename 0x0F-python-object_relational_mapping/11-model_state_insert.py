#!/usr/bin/python3
"""
 prints the State object with the name passed as argument from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main(username, password, dbname,):
    db_u = f"""mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"""
    engine = create_engine(db_u)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
