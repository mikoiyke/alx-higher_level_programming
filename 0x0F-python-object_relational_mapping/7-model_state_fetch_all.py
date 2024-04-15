#!/usr/bin/python3
"""
Write a script that lists all State objects from the database
"""

from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from model_state import Base, State

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all states ordered by their id
    all_states = session.query(State).order_by(State.id.asc()).all()
    for state in all_states:
        print(f"{state.id}: {state.name}")

    session.close()
