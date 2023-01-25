from fastapi import APIRouter
from db.db_connection import conn
router = APIRouter()

@router.post("/route")
def post_route_data(name, abrv, id):
    curs = conn.cursor()
    sql = f"INSERT INTO route(routeNm, routeAbrv, routeId) VALUES ('{name}', '{abrv}', {id})"
    curs.execute(sql)
    conn.commit()
    conn.close()
    return f"{name} created..."
