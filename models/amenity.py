#!/usr/bin/env python
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Public attributes:
        name (str): The name of the amenity.
    """

    name = ""
