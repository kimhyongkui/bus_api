from fastapi import APIRouter
from db.post.join import create_account

router = APIRouter()


@router.post('/join', tags=["create"])
def join(user_id: str, pwd: str):
    result = create_account(user_id, pwd)
    return result
