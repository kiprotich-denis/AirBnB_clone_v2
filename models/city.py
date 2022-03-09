#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
import os
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if (os.getenvb("HBNB_TYPE_STORAGE") == "db"):
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
        name = Column(String(128), nullable=False)
        place = relationship("Place", cascade='all')
    else:
        state_id = ""
        name = ""
