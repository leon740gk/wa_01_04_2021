from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://leon740gk:@localhost:5432/wa_test_02')
Session = sessionmaker(bind=engine)

Base = declarative_base()
