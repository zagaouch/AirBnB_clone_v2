#!/usr/bin/python3
""" Place Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer(), nullable=False)
    number_bathrooms = Column(Integer(), nullable=False)
    max_guest = Column(Integer(), nullable=False)
    price_by_night = Column(Integer(), nullable=False)
    latitude = Column(Float(), nullable=False)
    longitude = Column(Float(), nullable=False)
    reviews = relationship("Review", backref="place", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """Get reviews if storage if filestorage"""
            from models import storage
            from models.review import Review
            all_revs = storage.all(Review)
            plc_revs = all_revs
            for r in all_revs.values():
                if r.place_id == self.id:
                    plc_revs.append(r)
            return plc_revs

    # amenity_ids = []
