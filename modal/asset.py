from sqlalchemy import Column, String, SmallInteger, Integer
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from database.base import Base, Session


class Asset(Base):
    __tablename__ = 'asset'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    qty = Column(SmallInteger)

    def __init__(self, id, name, qty):
        self.id = id
        self.name = name
        self.qty = qty

    def __init__(self, name, qty):
        self.name = name
        self.qty = qty


def find_all():
    try:
        session = Session()
        result = session.query(Asset).all()

        session.close()

        return result
    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))

def find_by_name(name):
    try:
        session = Session()
        result = session.query(Asset).filter(Asset.name == name).first()
        session.close()
        
        return result
    except NoResultFound:
        return None
    
def total():
    try:
        session = Session()
        result = session.query(Asset).count()

        session.close()

        return result
    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))

def update(asset):
    try:
        session = Session()
        result = session.query(Asset).filter(Asset.id == asset.id).first()
        if result:
            result.name = asset.name
            result.qty = asset.qty

            session.commit()
            session.close()

    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))



def find_by_id(id):
    try:
        session = Session()
        result = session.query(Asset).filter(Asset.id == id).first()
        session.close()
        
        return result
    except NoResultFound:
        return None
    

def insert(asset):
    try:
        session = Session()
        session.add(asset)

        session.commit()
        session.close()
    except SQLAlchemyError as e:
        session.rollback()
        print("An error occurred:", str(e))
