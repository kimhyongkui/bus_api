from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import route_data, route_list, station
from fastapi import status, HTTPException

Session = sessionmaker(bind=engine)
session = Session()


def get_stn_data(stn_name, stn_id):
    try:
        result = session.query(route_data).filter_by(stnNm=f"{stn_name}", stnId=f"{stn_id}").all()
        if not result:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="잘못된 매개변수 입력")
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

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()


def get_route_data(route_name):
    try:
        result = session.query(route_data).filter(route_data.routeNm.like(f"%{route_name}%")).all()
        if not result:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="잘못된 매개변수 입력")
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

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()


def get_route_list(route_name=None):
    try:
        query = session.query(route_list)

        if route_name:
            result = query.filter_by(routeNm=route_name).first()
            if not result:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="잘못된 매개변수 입력")

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
        return result

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()


def get_stn_name(stn_name):
    try:
        result = session.query(station). \
            filter(station.stnNm.like(f"%{stn_name}%")).group_by(station.stnId).all()
        if not result:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="잘못된 매개변수 입력")
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
            return result

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()
