from sqlalchemy import Column, String, Date, SmallInteger, TIMESTAMP, ForeignKey, ARRAY, JSON
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.orm import relationship
from database.base import Base, Session


class Population(Base):
    __tablename__ = 'population'

    id = Column(String, primary_key=True)
    full_name = Column(String, nullable=False)
    other_name = Column(String)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(SmallInteger, nullable=False)
    born_location = Column(String)
    domicile = Column(String)
    temp_residence_addr = Column(ARRAY(JSON))
    perm_residence_addr = Column(ARRAY(JSON))
    job = Column(ARRAY(JSON))
    ethnic = Column(String)
    religion = Column(String)
    passport_number = Column(String)
    identification_number = Column(String)
    updated_date = Column(TIMESTAMP)

    household_id = Column(String, ForeignKey('household.id'))
    household = relationship('Household', foreign_keys=[household_id], lazy='subquery')

    relationship_with_householder = Column(SmallInteger)


def find_all():
    try:
        session = Session()
        households = session.query(Population).all()
        session.close()
        return households
    except NoResultFound:
        return None


def find_by_id(id):
    try:
        session = Session()
        result = session.query(Population).filter(Population.id == id).first()
        session.close()
        return result
    except NoResultFound:
        return None


def find_by_household(id):
    try:
        session = Session()
        result = session.query(Population).filter(Population.household_id == id).all()
        return result
    except NoResultFound:
        return None


def update_household_id(id, new_household_id):
    try:
        session = Session()
        result = session.query(Population).filter(Population.id == id).first()
        if result:
            result.household_id = new_household_id
            session.commit()

            session.close()

    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))