from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DbUser
from schemas import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        password = Hash.bcrypt(request.password),
        zp = request.zp,
        growdate = request.growdate,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Пользователь №{id} не найден',
        )
    return user

# def get_user_by_username(db: Session, username: str):
#     user = db.query(DbUser).filter(DbUser.username == username).first()
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f'Пользователь {username} не найден',
#         )
#     return user

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if user.count() == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Пользователь №{id} не найден',
        )
    user.update({
        DbUser.username: request.username,
        DbUser.password: Hash.bcrypt(request.password),
        DbUser.zp: request.zp,
        DbUser.growdate: request.growdate,
    })
    db.commit()
    res = user.first()
    db.refresh(res)
    return res

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Пользователь №{id} не найден',
        )
    db.delete(user)
    db.commit()
    return 'ok'