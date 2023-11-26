#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                       Column('place_id', String(60), ForeignKey("places.id"),
                              nullable=False, primary_key=True),
                       Column('amenity_id', String(60),
                              ForeignKey("amenities.id"),
                                         nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             backref="place_amenities", viewonly=False)

    def __init__(self, *args, **kwargs):
        """ Initialize class"""
        super().__init__(*args, **kwargs)

    if models.storage_type != 'db':

        @property
        def amenities(self):
            """ A getter to return list of amenity instances"""
            from models.amenity import Amenity
            amenities_l = []
            all_amenities = models.storage.all(Amenity)

            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenities_l.append(amenity)
            return amenities_l

        @property
        def reviews(self):
            """ A getter to return list of review instances"""
            from models.review import Review
            reviews_l = []
            all_reviews = models.storage.all(Review)

            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews_l.append(review)
            return reviews_l
