from sqlalchemy import Column, String, SmallInteger, Date
from database.base import Base
from database.base import Session
from sqlalchemy.orm.exc import NoResultFound


class General(Base):
    __tablename__ = 'general'

    id = Column(SmallInteger, primary_key=True)
    owner = Column(String)
    location = Column(String)
    from_year = Column(Date)
    to_year = Column(Date)


def find_general():
    try:
        session = Session()
        general = session.query(General).all()
        return general[0]
    except NoResultFound:
        return None