from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay, UserDisplayList
from db.database import get_db
from db import db_user
from auth.oauth2 import oauth2_scheme, get_user_by_token


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


@router.get('/', response_model=List[UserDisplayList], summary='Все пользователи')
def get_all_user(db: Session = Depends(get_db)):
    """
    Получение списка всех пользователей

    Returns:
        List[Dict]: Список пользователей
    """
    return db_user.get_all_users(db)


@router.get('/{id}', response_model=UserDisplay, summary='Пользователь №(id)')
def get_user(
        id: int,
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db),
        ):
    """
    Получение пользователя с заданным id

    **id (int)**: Идентификационный номер
    **token (bearer)**: Токен идентификации

    Returns:
        Dict: Имя пользователя, Зарплата, Дата повышения
    """
    token_user = get_user_by_token(db, token)
    if token_user and token_user.id == id:
        return token_user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.post('/{id}/update', response_model=UserDisplay, summary='Внесение изменений')
def update_user(
        id: int,
        request: UserBase,
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db),
        ):
    """
    **Внесение новых данных в запись (по id)**

    Request:
    - **id (int)**: Идентификационный номер

    Header:
    - **Authorization (bearer)**: Токен идентификации

    Body:
    - **username**: Имя пользователя
    - **password**: Пароль
    - **zp**: Зарплата
    - **growdate**: Дата повышения

    Returns:
        Результат записи
    """
    token_user = get_user_by_token(db, token)
    if token_user and token_user.id == id:
        return db_user.update_user(db, id, request)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.get('/{id}/delete', summary='Удаление пользователя')
def delete_user(
        id: int,
        token: Annotated[str, Depends(oauth2_scheme)],
        db: Session = Depends(get_db),
        ):
    """
    Удаление пользователя (по id)

    Request:
    - **id (int)**: Идентификационный номер

    Header:
    - **Authorization (bearer)**: Токен идентификации

    Returns:
        str: 'ok'
    """
    token_user = get_user_by_token(db, token)
    if token_user and token_user.id == id:
        return db_user.delete_user(db, id)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
