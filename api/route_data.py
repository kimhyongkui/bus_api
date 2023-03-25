import requests
import xmltodict
from dotenv import load_dotenv
import os
from db.get.db_data import get_route_list
from fastapi import status, HTTPException

load_dotenv()


# 특정 경유노선의 전체정류소 데이터 얻기
def get_route_data(route_id):
    try:
        url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?" \
              f"serviceKey={os.getenv('KEY')}&busRouteId={route_id}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']['itemList']
        route_data_list = []
        for route_data in data:
            route_data_dict = {
                'routeId': route_id,
                'routeNm': route_data['rtNm'],
                'stnOrd': route_data['staOrd'],
                'stnNm': route_data['stNm'],
                'stnId': route_data['stId']
            }
            route_data_list.append(route_data_dict)

        return route_data_list

    except TypeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='잘못된 매개변수 입력')

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))


# 모든 경유노선의 전체정류소 데이터 얻기
def get_all_route_data():
    route_data_list = []
    for route_id in get_route_list():
        try:
            data = get_route_data(route_id['routeId'])
            route_data_list.extend(data)
            print(route_id['routeId'])

        except HTTPException as err:
            print(f"{route_id['routeId']}:{err.detail}")
            continue

    return route_data_list
