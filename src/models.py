import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, primary_key=True)
    email = Column(String(30), Unique=True)
    password = Column(String(30), Unique=True, )
    name = Column(String(50))
    postDescription = Column(String(500))
    messengers = Column(String)

class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    postId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey = "Users.sersId")
    description = Column(String(500))
    comments = Column(String(200))
    messenger = Column(String)
    user = relationship(Users)

class Messengers(Base):
    __tablename__ = "messengers"
    messengerId = Column(Integer, primary_key = True)
    userId = Column(Integer, ForeignKey = "Users.userId")
    postId  = Column(Integer, ForeignKey = "Post.postId")
    messenger = Column(String)
    user = relationship(Users)
    post = relationship(Posts)

class Comments(Base):
    commentId = Column(Integer, primary_key = True)
    userId = Column(Integer, ForeignKey = "Users.userId")
    postId = Column(Integer, ForeignKey = "Post.postId")
    comment = Column(String(200))
    user = relationship(Users)
    post = relationship(Posts)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
