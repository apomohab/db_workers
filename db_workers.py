import os
import sys
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship 

Base = declarative_base()

class Factory(Base):

    __tablename__ = 'factory'

    

    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)


class Worker(Base):   

    __tablename__ = 'workers'  

    id     = Column(Integer, primary_key = True)
    name   = Column(String(80), nullable = False)
    age    = Column(String(25))
    special= Column(String(25))
    factory = relationship(Factory)
    factory_id = Column(Integer, ForeignKey('factory.id'))


engine = create_engine('sqlite:///paintfactory.db')
Base.metadata.create_all(engine)    

    
