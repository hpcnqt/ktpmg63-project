from datetime import datetime

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

    def __init__(self, id, full_name, other_name, date_of_birth, gender, born_location, ethnic, religion, id_number,
                 pp_number, updated_date):
        self.id = id
        self.full_name = full_name
        self.other_name = other_name
        self.date_of_birth = date_of_birth
        self.born_location = born_location
        self.gender = gender
        self.ethnic = ethnic
        self.religion = religion
        self.identification_number = id_number
        self.passport_number = pp_number
        self.updated_date = updated_date


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


def update(population):
    try:
        session = Session()
        result = session.query(Population).filter(Population.id == population.id).first()
        if result:
            result.full_name = population.full_name
            result.other_name = population.other_name
            result.date_of_birth = population.date_of_birth
            result.born_location = population.born_location
            result.gender = population.gender
            result.ethnic = population.ethnic
            result.religion = population.religion
            result.identification_number = population.identification_number
            result.passport_number = population.passport_number
            result.updated_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            session.commit()
            session.close()

    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))


def insert(population):
    try:
        session = Session()
        session.add(population)

        session.commit()
        session.close()
    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))


def total():
    try:
        session = Session()
        result = session.query(Population).count()

        session.close()

        return result
    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))
