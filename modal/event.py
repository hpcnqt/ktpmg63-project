from sqlalchemy import Column, String, SmallInteger, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
from database.base import Base
from database.base import Session


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner = Column(String)
    owner_contact = Column(String)
    fee = Column(Integer)
    status = Column(SmallInteger)
    from_time = Column(TIMESTAMP)
    to_time = Column(TIMESTAMP)

    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship('Department', foreign_keys=[department_id], overlaps='events', lazy='subquery')


def find_all():
    try:
        session = Session()
        result = session.query(Event).all()

        session.close()

        return result

    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))


def find_by_id(id):
    try:
        session = Session()
        result = session.query(Event).filter(Event.id == id).first()

        session.close()

        return result

    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))
