#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if (os.getenvb("HBNB_TYPE_STORAGE") == "db"):
        name = Column(String(128), nullable=False)
    else:
        name = ""
