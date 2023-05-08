from api.route import get_all_route_list
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Route_list
from dotenv import load_dotenv
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 각 노선의 아이디와 이름 DB저장
def add_route_list():
    try:
        for data in get_all_route_list():
            result = Route_list(
                routeNm=data['routeNm'],
                routeAbrv=data['routeAbrv'],
                routeId=data['routeId']
            )
            session.add(result)
        session.commit()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 저장 완료"})

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()
