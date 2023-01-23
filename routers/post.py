from fastapi import APIRouter
from db.db_connection import conn
router = APIRouter()

@router.post("/route")
def post_route_data(name, id):
    curs = conn.cursor()
    sql = f"INSERT INTO route (routeNm, routeId) VALUES ({name}, {id})"
    curs.execute(sql)
    conn.commit()
    conn.close()
    return f"{name} created..."
