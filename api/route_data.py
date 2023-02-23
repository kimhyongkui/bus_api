import requests
import xmltodict
from dotenv import load_dotenv
import os
from api.route import get_all_route_list

load_dotenv()


# 특정 경유노선의 전체정류소 데이터 얻기
def get_route_data(route_id):
    try:
        url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?" \
              f"serviceKey={os.getenv('key')}&busRouteId={route_id}"
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

    except Exception as err:
        return f"{err}, 노선ID를 확인하세요"


# 모든 경유노선의 전체정류소 데이터 얻기
def get_all_route_data():
    try:
        route_data = get_all_route_list()
        route_data_list = []
        for route in route_data:
            route_data_list.append(get_route_data(route['routeId']))
            print(f"{route['routeId']}번 노선의 데이터를 추가했습니다")
        return route_data_list

    except Exception as err:
        return f"{err}, 오류가 난 노선ID를 확인하세요"
