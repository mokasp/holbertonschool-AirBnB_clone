#!/usr/bin/python3
""" Module containing the class Place """
# Michael 1:54 PM 10/7
import BaseModel


class Place(BaseModel):
    """
    A class called Place with a public attributes.

    Attributes
    ~~~~~~~~~~
        city_id (string):
            ID of city
        user_id (string):
            ID of user
        name (string):
            Name of the place
        description (string):
            Description of place
        number_rooms (integer):
            Number of rooms at place
        number_bathrooms (integer):
            Number of bathrooms at place
        max_guest (integer):
            Max number of guests
        price_by_night (integer):
            Price per night
        latitude (float 0.0)
            Latitude of place
        longitude (float 0.0)
            Longitude of place
        amenity_ids (list of strings):
            All amenities offered listed by ID
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []
