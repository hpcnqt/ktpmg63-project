from sqlalchemy import Column, String, SmallInteger
from database.base import Base
from database.base import Session
from sqlalchemy.orm.exc import NoResultFound


class Account(Base):
    __tablename__ = 'account'

    id = Column(SmallInteger, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String)
    password = Column(String, nullable=False)


def string_adjust(string: str, desired_length ):
    if len(string) < desired_length:
        padded_string = string.ljust(desired_length)
    else:
        padded_string = string

    return padded_string


def find_by_username(username):
    try:
        session = Session()
        account = session.query(Account).filter(Account.username == string_adjust(username, 50)).first()
        return account
    except NoResultFound:
        return None
