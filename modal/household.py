from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, Date
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.orm import relationship
from database.base import Base, Session
from datetime import datetime


class Household(Base):
    __tablename__ = 'household'

    id = Column(String, primary_key=True)
    house_number = Column(String)
    street_hamlet = Column(String)
    commune_ward = Column(String)
    city_district_town = Column(String)
    province = Column(String)
    register_date = Column(Date)
    updated_date = Column(TIMESTAMP)

    householder_id = Column(String, ForeignKey('population.id'))
    householder = relationship('Population', foreign_keys=[householder_id], lazy='subquery')

    def __init__(self, id, house_number, street_hamlet, commune_ward, city_district_town
                 , province, register_date, updated_date, householder_id):
        self.id = id
        self.house_number = house_number
        self.street_hamlet = street_hamlet
        self.commune_ward = commune_ward
        self.city_district_town = city_district_town
        self.province = province
        self.register_date = register_date
        self.updated_date = updated_date
        self.householder_id = householder_id


def find_all():
    try:
        session = Session()
        households = session.query(Household).all()
        session.close()
        return households
    except NoResultFound:
        return None


def find_by_id(id):
    try:
        session = Session()
        result = session.query(Household).filter(Household.id == id).first()
        session.close()
        return result
    except NoResultFound:
        return None


def update(household):
    try:
        print(household.id, 'household')

        session = Session()
        result = session.query(Household).filter(Household.id == household.id).first()

        if result:
            result.house_number = household.house_number
            result.street_hamlet = household.street_hamlet
            result.commune_ward = household.commune_ward
            result.city_district_town = household.city_district_town
            result.province = household.province
            result.register_date = household.register_date
            result.householder_id = household.householder_id
            result.updated_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            session.commit()
            print("OK")

            session.close()

    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))


def insert(household):
    try:
        session = Session()
        session.add(household)
        session.commit()

        session.close()
    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))


def total():
    try:
        session = Session()
        result = session.query(Household).count()
        session.close()
        return result
    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))