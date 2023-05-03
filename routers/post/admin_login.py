from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from db.create.login import login

router = APIRouter()


@router.post("/login", tags=["login"])
def login_jwt(form_data: OAuth2PasswordRequestForm = Depends()):
    result = login(form_data.username, form_data.password)
    return result
