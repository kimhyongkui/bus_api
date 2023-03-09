from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import route_data, route_list, station
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()


def get_stn_data(stn_name, stn_id):
    try:
        result = session.query(route_data).filter_by(stnNm=f"{stn_name}", stnId=f"{stn_id}").all()
        if not result:
            raise HTTPException(status_code=204, detail="Data가 없음")
        else:
            data_list = []
            for data in result:
                data_dict = {
                    'routeId': data.routeId,
                    'routeNm': data.routeNm,
                    'stnOrd': data.stnOrd,
                    'stnNm': data.stnNm,
                    'stnId': data.stnId
                }
                data_list.append(data_dict)
            result = data_list
        return result

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()

# print(get_stn_data('가좌역', 113000496))
print(get_stn_data('가좌역', 11300049))

def get_route_data(route_name):
    try:
        result = session.query(route_data).filter(route_data.routeNm.like(f"%{route_name}%")).all()
        if not result:
            result = JSONResponse(content={"message": "데이터가 없습니다"}, status_code=status.HTTP_201_CREATED)
        else:
            data_list = []
            for data in result:
                data_dict = {
                    'routeId': data.routeId,
                    'routeNm': data.routeNm,
                    'stnOrd': data.stnOrd,
                    'stnNm': data.stnNm,
                    'stnId': data.stnId
                }
                data_list.append(data_dict)
            result = JSONResponse(content=data_list, status_code=status.HTTP_200_OK)

    except Exception as err:
        result = JSONResponse(content={"message": f"{err}, 다시 검색하세요"}, status_code=status.HTTP_404_NOT_FOUND)

    finally:
        session.close()

    return result


def get_route_list(route_name=None):
    try:
        query = session.query(route_list)

        if route_name:
            result = query.filter_by(routeNm=route_name).first()
            if not result:
                result = '데이터가 없습니다. 다시 검색하세요'

            else:
                result_dict = {
                    'routeNm': result.routeNm,
                    'routeAbrv': result.routeAbrv,
                    'routeId': result.routeId
                }
                result = result_dict

        else:
            result = query.all()
            data_list = []
            for data in result:
                data_list.append({
                    'routeNm': data.routeNm,
                    'routeAbrv': data.routeAbrv,
                    'routeId': data.routeId
                })
            result = data_list

    except Exception as err:
        result = f"{err}, 노선 이름을 확인하세요"

    finally:
        session.close()

    return result


def get_stn_name(stn_name):
    try:
        result = session.query(station). \
            filter(station.stnNm.like(f"%{stn_name}%")).group_by(station.stnId).all()
        if not result:
            result = '데이터가 없습니다.'
        else:
            data_list = []
            for data in result:
                data_dict = {
                    'stnNm': data.stnNm,
                    'stnId': data.stnId,
                    'arsId': data.arsId,
                    'direction': data.direction
                }
                data_list.append(data_dict)
            result = data_list

    except Exception as err:
        result = f"{err}, 다시 검색하세요"

    finally:
        session.close()

    return result
