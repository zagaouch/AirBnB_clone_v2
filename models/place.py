#!/usr/bin/python3
""" Place Module for HBNB project """


from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer(), nullable=False, default=0)
        number_bathrooms = Column(Integer(), nullable=False, default=0)
        max_guest = Column(Integer(), nullable=False, default=0)
        price_by_night = Column(Integer(), nullable=False, default=0)
        latitude = Column(Float(), nullable=True)
        longitude = Column(Float(), nullable=True)
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 overlaps="place_amenities",
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        reviews = []
        amenity_ids = []

        @property
        def amenities(self):
            """Get amenities if storage if filestorage"""
            from models import storage
            from models.amenity import Amenity
            all_amenities = storage.all(Amenity)
            plc_amenities = []
            for a in all_amenities.values():
                if a.id in self.amenity_ids:
                    plc_amenities.append(a)
            return plc_amenities

        @amenities.setter
        def amenities(self, obj):
            """Set amenities if storage if filestorage"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)

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
