from fastapi import APIRouter
from db.connection import conn

router = APIRouter()


@router.put('/route')
def patch_data(table, column, patch_val, value):
    curs = conn.cursor()
    sql = f"UPDATE {table} SET {column}='{patch_val}' WHERE {column}='{value}'"
    curs.execute(sql)
    conn.commit()

    return f"{table} {column} {value}->{patch_val} updated..."
