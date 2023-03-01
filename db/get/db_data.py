from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import route_data, route_list, station

Session = sessionmaker(bind=engine)
session = Session()


def get_stn_data(stn_name, stn_id):
    try:
        result = session.query(route_data). \
            filter(route_data.stnNm == f"{stn_name}", route_data.stnId == f"{stn_id}").all()
        if not result:
            result = '데이터가 없습니다. 다시 검색하세요'
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

    except Exception as err:
        result = f"{err}, 정류소 이름 또는 ID를 확인하세요"

    finally:
        session.close()

    return result


# print(get_stn_data('안암역', 107000205))

def get_route_data(route_name):
    try:
        result = session.query(route_data).filter(route_data.routeNm.like(f"%{route_name}%")).all()
        if not result:
            result = '다시 검색하세요'

    except Exception as err:
        result = f"{err}, 다시 검색하세요"

    finally:
        session.close()

    return result


def get_route_list(route_name):
    try:
        result = session.query(route_list).filter(route_list.routeNm.like(f"%{route_name}%")).first()
        if not result:
            result = '데이터가 없습니다. 다시 검색하세요'

        else:
            data_list = []
            for data in result:
                data_dict = {
                    'routeNm': data.routeNm,
                    'routeAbrv': data.routeAbrv,
                    'routeId': data.routeId
                }
                data_list.append(data_dict)
            result = data_list

    except Exception as err:
        result = f"{err}, 노선 이름을 확인하세요"

    finally:
        session.close()

    return result


print(get_route_list(6001))


def get_stn_name(stn_name):
    try:
        result = session.query(station.stnNm, station.stnId, station.arsId, station.direction). \
            filter(station.stnNm.like(f"%{stn_name}%")).group_by(station.stnId).all()
        if not result:
            result = '다시 검색하세요'

    except Exception as err:
        result = f"{err}, 다시 검색하세요"

    finally:
        session.close()

    return result
