#!/usr/bin/python3
"""creating a new engine de_storage"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State


class DBStorage:
    """A database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initializing new instance"""
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    os.environ.get("HBNB_MYSQL_USER"),
                    os.environ.get("HBNB_MYSQL_PWD"),
                    os.environ.get("HBNB_MYSQL_HOST"),
                    os.environ.get("HBNB_MYSQL_DB")
                ),
                pool_pre_ping=True
            )
        if os.environ.get("HBNB_ENV") == 'test':
            base.meta.drop_all(self.__engine)
            
    def all(self, cls=None):
        """query all data base"""
        if cls:
            query = self.__session.query(cls).all()
        else:
            query = self.__session.query(State).all()
            query.extend(self.__session.query(City).all())
            query.extend(self.__session.query(User).all())
            query.extend(self.__session.query(Place).all())
            query.extend(self.__session.query(Review).all())
            query.extend(self.__session.query(State).all())
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in query}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all the tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False, )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ public method def close(self):: call remove() method
        on the private session attribute (self.__session)
        """
        if self.__session:
            self.__session.close()
