from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import route_data, route_list, station, vehicle

Session = sessionmaker(bind=engine)

def get_stn_data(stn_name, stn_id):
    session = Session()
    try:
        result = session.query(route_data).filter_by(stnNm=stn_name, stnId=stn_id).all()

        if not result:
            result = '데이터가 없습니다. 다시 검색하세요'

    except Exception as err:
        result = f"{err}, 정류소 이름 또는 ID를 확인하세요"

    finally:
        session.close()

    return result


def get_route_data(route_name):
    session = Session()
    try:
        result = session.execute(
            f"SELECT routeNm, stnOrd, stnNm FROM route_data WHERE routeNm Like '%{route_name}%'").fetchall()

        if not result:
            result = '다시 검색하세요'

    except Exception as err:
        result = f"{err}, 다시 검색하세요"

    finally:
        session.close()


    return result


def get_route_list(route_name):
    session = Session()
    try:
        result = session.execute(f"SELECT * FROM route_list WHERE routeNm Like '%{route_name}%'").fetchone()

        if not result:
            result = '데이터가 없습니다. 다시 검색하세요'

    except Exception as err:
        result = f"{err}, 노선 이름을 확인하세요"

    finally:
        session.close()


    return result


def get_stn_name(stn_name):
    session = Session()
    try:
        result = session.execute(f"SELECT stnNm, stnId, arsId, direction FROM station WHERE stnNm Like '%{stn_name}%' GROUP BY stnId").fetchall()

        if not result:
            result = '다시 검색하세요'

    except Exception as err:
        result = f"{err}, 다시 검색하세요"

    finally:
        session.close()


    return result
