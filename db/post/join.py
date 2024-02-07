from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Account
from fastapi import HTTPException, status
from app.auth.password import password_hash
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def create_account(user_id, pwd):
    try:
        if session.query(Account).filter_by(user_id=user_id).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="중복된 아이디.")

        account = Account(
            user_id=user_id,
            pwd=password_hash(pwd),
            permission=True
        )
        session.add(account)
        session.commit()

        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "계정 생성 완료"})

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()
