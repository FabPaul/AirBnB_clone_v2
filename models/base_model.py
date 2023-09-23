#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """
    BaseModel class defining common attributes/methods for other classes
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Instantiation of the BaseModel class

        Args:
            args: Not used
            kwargs: Arguments for the constructor of the BaseModel

        Attributes:
            id (str): Unique id generated
            created_at (datetime): Creation date
            updated_at (datetime): Updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = datetime.now()

                if 'created_at' in kwargs and 'updated_at' not in kwargs:
                    self.updated_at = self.created_at
                else:
                    self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation

        Returns:
            str: A string containing class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """
        Return a string representation

        Returns:
            str: A string representation
        """
        return self.__str__()

    def save(self):
        """
        Update the public instance attribute updated_at to the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Create a dictionary representation of the class

        Returns:
            dict: A dictionary containing key-value pairs from __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        if '_sa_instance_state' in my_dict:
            my_dict.pop('_sa_instance_state')

        return my_dict

    def delete(self):
        """
        Delete the current instance from the model storage
        """
        models.storage.delete(self)
