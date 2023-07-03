from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError

from database.base import Base
from database.base import Session


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    events = relationship('Event', lazy='subquery')


def find_all():
    try:
        session = Session()
        result = session.query(Department).all()

        session.close()

        return result
    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))
