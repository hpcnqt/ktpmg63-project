from sqlalchemy import Column, String, SmallInteger, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
from database.base import Base
from database.base import Session

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    owner = Column(String)
    owner_contact = Column(String)
    fee = Column(Integer)
    status = Column(SmallInteger)
    from_time = Column(TIMESTAMP)
    to_time = Column(TIMESTAMP)

    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship('Department', foreign_keys=[department_id], overlaps='events', lazy='subquery')

    def __init__(self, name, owner, contact, fee, status, from_time, to_time, department_id):
        self.name = name
        self.owner = owner
        self.owner_contact = contact
        self.fee = fee
        self.from_time = from_time
        self.to_time = to_time
        self.department_id = department_id
        self.status = status

    @classmethod
    def from_id(cls, id):
        session = Session()
        obj = session.query(cls).get(id)
        session.close()
        return obj


def find_all():
    try:
        session = Session()
        result = session.query(Event).all()

        session.close()

        return result

    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))


def delete(event):
    try:
        session = Session()
        session.delete(event)
        session.commit()
        session.close()
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


def update(event):
    try:
        session = Session()
        result = session.query(Event).filter(Event.id == event.id).first()

        if result:
            result.name = event.name
            result.owner = event.owner
            result.owner_contact = event.owner_contact
            result.fee = event.fee
            result.status = event.status
            result.from_time = event.from_time
            result.to_time = event.to_time
            result.department_id = event.department_id

            session.commit()
            session.close()

    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))


def update_status(event):
    try:
        session = Session()
        result = session.query(Event).filter(Event.id == event.id).first()

        if result:
            result.status = 1
            session.commit()

            session.close()

    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))


def insert(event):
    try:
        session = Session()
        session.add(event)
        session.commit()

        session.close()
    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))
