#!/usr/bin/pythoni3
"""Module: Data Base storage of data"""

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os


class DBStorage:
    """Database base storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize an instance"""
        msqluser = os.getenv('HBNB_MYSQL_USER')
        msqlpwd = os.getenv('HBNB_MYSQL_PWD')
        msqlhost = os.getenv('HBNB_MYSQL_HOST')
        msql_db = os.getenv('HBNB_MYSQL_DB')
        hbnb_env = os.getenv('HBNB_ENV')

        db_url = f"mysql+mysqldb://{msqluser}:{msqlpwd}@{msqlhost}/{msql_db}"

        if hbnb_env == 'test':
            self.__engine = create_engine(db_url, pool_pre_ping=True)
            metadata = MetaData()
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(self.__engine)
        else:
            self.__engine = create_engine(db_url, pool_pre_ping=True)

    def all(self, cls=None):
        """Query on the current database session"""
        result = {}
        
        if cls is None:
            classes_to_query = [State, City]
            for class_obj in classes_to_query:
                query_result = self.__session.query(class_obj).all()
                for obj in query_result:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    result[key] = obj
        else:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj

        return result

    def new(self, obj):
        """Add a new instance to the database"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Remove an instance from the database if obj not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the session // reset the database"""
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

