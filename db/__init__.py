import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# set database URL
base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(base_dir, 'dev.db')

# create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# describe tables and mapping
Base = declarative_base()

# create ORM session explicitly
Session = sessionmaker(bind=engine)
session = Session()


