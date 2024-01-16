"""
This module defines the DBStorage class
"""

from sqlalchemy import create_engine, sessionmaker
import os
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User



class DBStorage:
    """DBStorage class that connects to local mysql database"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine  = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                        user, pwd, host, db), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = sessionmaker(bind=self.__engine)
        
    def all(self, cls=None):
        """
            Returns all objects in the database dpendeding on cls,
            if cls is None, returns all objects nomatter the class,
            if cls is a , returns objs of class a
        """

        all_classes = [User, State, City, Amenity, Place, Review]
        result = {}

        if cls is None:
            classes = all_classes
        else:
            classes = [cls]
        for cls in classes:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj