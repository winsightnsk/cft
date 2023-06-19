from src.db.database import dec_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, Float

class DbUser(dec_base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    fee = Column(Float)
