#!/usr/bin/python3
"""
Database Engine for AirBnB
"""

from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


class DBStorage:
    """
    Database storage class for AirBnB
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize the database connection and engine
        """

        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}',
            pool_pre_ping=True
        )

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query the database and return a dictionary of objects

        Args:
            cls (class): The class to query for. If None, query all classes

        Returns:
            dict: A dictionary of objects
        """

        all_classes = [Amenity, City, Place, Review, State, User]
        entities = dict()

        if cls is None:
            for entity in all_classes:
                query = self.__session.query(entity)
                for obj in query.all():
                    entity_key = f'{obj.__class__.__name__}.{obj.id}'
                    entities[entity_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                entity_key = f'{obj.__class__.__name__}.{obj.id}'
                entities[entity_key] = obj

        return entities

    def new(self, obj):
        """
        Add an object to the current database session

        Args:
            obj (BaseModel): The object to add
        """

        self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the current database session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session

        Args:
            obj (BaseModel): The object to delete
        """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and initialize a new session
        """

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Close the database session
        """

        self.__session.close()
