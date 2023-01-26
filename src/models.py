import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

class Planet(Base):
    __tablename__="planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(120),nullable=False)
    diameter = Column(Integer(),nullable=False)
    rotation_period = Column(Integer())
    orbital_period = Column(Integer())
    gravity = Column(Integer(),nullable=False)
    terrain = Column(String(120),nullable=False)
    surface_water = Column(Integer())
    population = Column(Integer())
    climate = Column(String(120),nullable=False)
    url = Column(String(120),nullable=False)
    created = Column(Integer(),nullable=False)
    edited = Column(Integer(),nullable=False)
    created_by_id=Column(Integer,ForeignKey("user.id",ondelete="cascade"))
    created_by=relationship(User, cascade="all, delete", passive_deletes=True)
  
class People(Base):
    __tablename__="people"
    id = Column(Integer, primary_key=True)
    name = Column(String(120),nullable=False)
    birth_year = Column(String(120),nullable=False)
    eye_color = Column(String(120),nullable=False)
    gender = Column(String(120),nullable=False)
    hair_color = Column(String(120),nullable=False)
    height = Column(Integer())
    mass = Column(Integer())
    skin_color = Column(String(120),nullable=False)
    homeworld_by_id = Column(Integer, ForeignKey("planet.id",ondelete="cascade"))
    homeworld = relationship(Planet,cascade="all, delete", passive_deletes=True)
    url = Column(String(120),nullable=False)
    created = Column(Integer(),nullable=False)
    edited = Column(Integer(),nullable=False)


class Vehicle(Base):
    __tablename__="vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(120),nullable=False)
    Base = Column(String(120),nullable=False)
    vehicle_class = Column(String(120),nullable=False)
    manufacturer = Column(String(120),nullable=False)
    length = Column(Integer())
    cost_in_credits = Column(Integer())
    crew = Column(String(120),nullable=False)
    passengers = Column(Integer())
    cargo_capacity = Column(Integer())
    url = Column(String(120),nullable=False)
    created = Column(Integer(),nullable=False)
    edited = Column(Integer(),nullable=False)
   

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
