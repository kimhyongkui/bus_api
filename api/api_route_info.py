import requests
import xmltodict
from dotenv import load_dotenv
import os
from api.api_route import get_route_all


load_dotenv()
key = os.getenv('key')

# arr = arrival

# 특정 경유노선의 전체정류소 데이터 얻기
def get_route_info(routeid):
    url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?" \
          f"serviceKey={key}&busRouteId={routeid}"
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    data = dict['ServiceResult']['msgBody']['itemList']
    arrive_list = []
    for arrive in range(len(data)):
        arrive_dict = {}
        arrive_dict['routeId'] = routeid
        arrive_dict['routeNm'] = data[arrive]['rtNm']
        arrive_dict['stnOrd'] = data[arrive]['staOrd']
        arrive_dict['stnNm'] = data[arrive]['stNm']
        arrive_dict['stnId'] = data[arrive]['stId']
        arrive_list.append(arrive_dict)
    return arrive_list



# 모든 경유노선의 전체정류소 데이터 얻기
def get_route_info_all():
    route_list = get_route_all()
    arrive_list = []
    for route in route_list:
        url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?" \
              f"serviceKey={key}&busRouteId={route['routeId']}"
        content = requests.get(url).content
        dict = xmltodict.parse(content)
        data = dict['ServiceResult']['msgBody']['itemList']
        for arrive in range(len(data)):
            arrive_dict = {}
            arrive_dict['routeId'] = route['routeId']
            arrive_dict['routeNm'] = data[arrive]['rtNm']
            arrive_dict['stnOrd'] = data[arrive]['staOrd']
            arrive_dict['stnNm'] = data[arrive]['stNm']
            arrive_dict['stnId'] = data[arrive]['stId']
            arrive_list.append(arrive_dict)
    return arrive_list








