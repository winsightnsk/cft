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