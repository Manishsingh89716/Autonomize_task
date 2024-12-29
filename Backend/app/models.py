from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

'''define models of the database i.e table and columns'''
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    location = Column(String)
    bio = Column(String)
    public_repos = Column(Integer)
    following = Column(Integer)
    followers = Column(Integer)
    active = Column(Boolean, default=True)