from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.envloader import DSL

dsl = DSL()

DATABASE_URL = "postgresql+psycopg2://{user}:{passw}@{host}:{port}/{dbname}".format(
    user=dsl.user,
    passw=dsl.password,
    host=dsl.host,
    port=dsl.port,
    dbname=dsl.dbname,
)

engine = create_engine(
    DATABASE_URL,
    connect_args={'check_thame_thread': False}
)

sessionlocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

dec_base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()






import psycopg2
from contextlib import contextmanager


@contextmanager
def pg_context(dsl: dict):
    """
    Генерация подглючения к Postgres

    Args:
        dsl (dict): Параметры подключения

    Yields:
        [Открытое соединение, курсор,]
    """
    conn = psycopg2.connect(**dsl)
    cur = conn.cursor()
    try:
        yield [conn, cur,]
    finally:
        cur.close()
        conn.close()