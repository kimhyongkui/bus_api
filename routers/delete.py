from fastapi import APIRouter
from db.db_connection import conn

router = APIRouter()

@router.delete("/route")
def delete_data(table, column, value):
    curs = conn.cursor()
    sql = f"DELETE FROM {table} WHERE {column} = '{value}'"
    curs.execute(sql)
    conn.commit()


    return f"{table}의 {column}의 {value} 삭제"

