#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class Amenity(BaseModel, Base):
    """ Implements the amenity model"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

