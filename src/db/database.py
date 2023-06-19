import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://root:pass@localhost/mydb".format(
    host=os.environ.get('DB_HOST')
)