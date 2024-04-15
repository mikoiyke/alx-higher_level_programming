#!/usr/bin/python3
"""Module Docs"""

if __name__ == '__ main__':
    from sys import argv
    from sqlalchemy import create_engine
    from model_state import Base, State

    db_url = (f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhot:3306/argv[3]"
             )
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print (f"{state.id}: {state.name}")
    session.close()
