#!/usr/bin/python3
"""
This is the DB storage class for AirBnB.
"""

import os
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

ALL_CLASSES = {"State", "City", "Amenity", "User", "Place", "Review"}


class DBStorage:
    """
    Database storage class for AirBnB

    Attributes:
        __engine: The SQLAlchemy engine
        __session: The SQLAlchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize a connection with MySQL and create tables
        """

        db_uri = f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}: \
                {getenv('HBNB_MYSQL_PWD')}@{getenv('HBNB_MYSQL_HOST')}: \
                3306/{getenv('HBNB_MYSQL_DB')}"
        self.__engine = create_engine(db_uri, pool_pre_ping=True)
        self.reload()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Return all objects of a specified class or all classes if cls is None
        """
        entities = dict()

        if cls:
            return self.get_data_from_table(cls, entities)

        for entity in ALL_CLASSES:
            entities = self.get_data_from_table(eval(entity), entities)

        return entities

    def new(self, obj):
        """
        Add obj to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and initialize a new session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def get_data_from_table(self, cls, structure):
        """
        Get the data from a MySQL table
        """
        if isinstance(structure, dict):
            query = self.__session.query(cls)

            for row in query.all():
                key = f"{cls.__name__}.{row.id}"
                structure[key] = row

            return structure

    def close(self):
        """
        Close the current session if running
        """
        self.__session.close()
