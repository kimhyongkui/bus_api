import requests
import xmltodict
from dotenv import load_dotenv
import os
from api.route import get_route_all

load_dotenv()


# 특정 경유노선의 전체정류소 데이터 얻기
def get_route_info(routeid):
    try:
        url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?" \
              f"serviceKey={os.getenv('key')}&busRouteId={routeid}"
        content = requests.get(url).content
        dict = xmltodict.parse(content)
        data = dict['ServiceResult']['msgBody']['itemList']
        arrive_list = []
        for arrive in range(len(data)):
            arrive_dict = {
                'routeId': routeid,
                'routeNm': data[arrive]['rtNm'],
                'stnOrd': data[arrive]['staOrd'],
                'stnNm': data[arrive]['stNm'],
                'stnId': data[arrive]['stId']
            }
            arrive_list.append(arrive_dict)
        return arrive_list

    except TypeError as err:
        return f"{err}, 노선ID를 확인하세요"

# 모든 경유노선의 전체정류소 데이터 얻기
def get_route_info_all():
    try:
        route_list = get_route_all()
        arrive_list = []
        for route in route_list:
            arrive_list.append(get_route_info(route['routeId']))
        return arrive_list

    except TypeError as err:
        return f"{err}, 오류가 난 노선ID를 확인하세요"