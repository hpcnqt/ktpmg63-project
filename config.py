class AppConfig:
    DEBUG = False
    SECRET_KEY = '20200563'


class DatabaseConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://userktpm:admin@localhost:5433/ktpmg63_db'