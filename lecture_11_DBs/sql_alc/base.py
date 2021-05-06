from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://leon740gk:@localhost:5432/wa_test')
Session = sessionmaker(bind=engine)

Base = declarative_base()

# This code creates:
# a SQLAlchemy Engine that will interact with our dockerized PostgreSQL database,
# a SQLAlchemy ORM session factory bound to this engine,
# and a base class for our classes definitions.

