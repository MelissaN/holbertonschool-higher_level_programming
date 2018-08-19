#!/usr/bin/python3
"""
use table relationship to access and print city and state
parameters given to script: username, password, database
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # use table relationship to access and print city and state
    rows = session.query(City).order_by(City.id).all()
    for city in rows:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
