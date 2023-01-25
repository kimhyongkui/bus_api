from fastapi import APIRouter
from db.db_connection import conn
router = APIRouter()

@router.put("/route")
def patch_data():
    curs = conn.cursor(table, column, value1, value2)
    sql = f"UPDATE {table} SET {column}='{value1}' WHERE {column}='{value2}'"
    curs.execute(sql)
    conn.commit()
    conn.close()

    return f"{table} {column} {value2}->{value1} updated..."


