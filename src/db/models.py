from db.database import dec_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, Float, String, DATE


class DbUser(dec_base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    zp = Column(Float)
    growdate = Column(DATE)
