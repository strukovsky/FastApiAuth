from sqlalchemy import Table, Integer, String, ForeignKey, create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///data.db")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    timestamp = Column(Integer)

Base.metadata.create_all()
