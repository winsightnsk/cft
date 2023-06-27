from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from envloader import DSL

load_dotenv()
dsl = DSL()

DATABASE_URL = "postgresql+psycopg2://{user}:{passw}@{host}:{port}/{dbname}".format(
    user=dsl.user,
    passw=dsl.password,
    host=dsl.host,
    port=dsl.port,
    dbname=dsl.dbname,
)

engine = create_engine(DATABASE_URL)

sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

dec_base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
