from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL='sqlite:///todoapp.db'
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread': False})

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine) #Bind ot the engine and autocommit and autoflush is disabled, to avoid randod
#commits


Base=declarative_base() # Create tables and it's objects





