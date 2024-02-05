#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

        if getenv('HBNB_TYPE_STORAGE') != 'db':
            @property
            def cities(self):
                """Getter attribute in case of file storage"""
                from models import storage
                from models.city import City

                city_list = []
                for city in storage.all(City).values():
                    if city.state_id == self.id:
                        city_list.append(city)
                return city_list
    else:
        name = ""
        cities = ""
