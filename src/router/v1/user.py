from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix='/api/v1/user',
    tags=['Пользователи']
)

@router.post('/', response_model=UserDisplay, summary='Новый пользователь')
def create_user(request: UserBase, db: Session = Depends(get_db)):
    """
    Создание нового пользователя

    - **username**: Имя пользователя
    - **password**: Пароль
    - **zp**: Зарплата
    - **growdate**: Дата повышения

    Returns:
        Результат записи
    """
    return db_user.create_user(db, request)

@router.get('/', response_model=List[UserDisplay], summary='Все пользователи')
def get_all_user(db: Session = Depends(get_db)):
    """
    Получение списка всех пользователей

    Returns:
        List[Dict]: Список пользователей
    """
    return db_user.get_all_users(db)

@router.get('/{id}', response_model=UserDisplay, summary='Пользователь №(id)')
def get_user(id: int, db: Session = Depends(get_db)):
    """
    Получение пользователя с заданным id

    **id (int)**: Идентификационный номер

    Returns:
        Dict: Имя пользователя, Зарплата, Дата повышения
    """
    return db_user.get_user(db, id)

@router.post('/{id}/update', response_model=UserDisplay, summary='Внесение изменений')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    """
    Внесение новых данный в запись (по id)

    - **username**: Имя пользователя
    - **password**: Пароль
    - **zp**: Зарплата
    - **growdate**: Дата повышения

    Returns:
        Результат записи
    """
    return db_user.update_user(db, id, request)

@router.get('/{id}/delete', summary='Удаление пользователя')
def delete_user(id: int, db: Session = Depends(get_db)):
    """
    Удаление пользователя (по id)

    - **id (int)**: Идентификационный номер

    Returns:
        str: 'ok'
    """
    return db_user.delete_user(db, id)