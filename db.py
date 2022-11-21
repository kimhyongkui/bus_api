from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os

load_dotenv()


user_name = 'root'
user_pwd = os.getenv('user_pwd')
db_host = '127.0.0.1'
db_name = 'prac'

DATABASE = f'mysql+pymysql://root:{user_pwd}@localhost:3306/prac'

ENGINE = create_engine(
    DATABASE,
    encoding='utf-8',
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()