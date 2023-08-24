#!/usr/bin/python3
""" This is """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """ This is class """
    __engine = None
    __session = None

    def __init__(self):
        """ Instane class """
        MySQL_user = getenv('HBNB_MYSQL_USER')
        MySQL_pwd = getenv('HBNB_MYSQL_PWD')
        MySQL_host = getenv('HBNB_MYSQL_HOST')
        MySQL_db = getenv('HBNB_MYSQL_DB')
        MySQL_env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            MySQL_user, MySQL_pwd, MySQL_host, MySQL_db), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if MySQL_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Show all class objecs if given
        """
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review, Amenity]
            objects = []
            for c in classes:
                objects += self.__session.query(c)
        my_dict = {}
        for obj in objects:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """ Add thession """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commit ale session """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete frof not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all engine """
        # Base.metadata.create_all(self.__engine)  # redundant with __init__?
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Closing `storage` with current state of DB.
        Project: 0am
        """
        self.__session.close()
