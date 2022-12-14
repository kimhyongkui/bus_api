import requests
import xmltodict
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')

# 노선번호에 해당하는 노선 목록 조회
url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={key}"

content = requests.get(url).content  # GET요청
dict = xmltodict.parse(content)  # XML을 dictionary로 파싱

data = dict['ServiceResult']['msgBody']['itemList']


def get_route_all():
    route_list = []
    for route in range(len(data)):
        route_dict = {}
        route_dict["routeNm"]= data[route]["busRouteNm"]
        route_dict["routeAbrv"] = data[route]["busRouteAbrv"]
        route_dict["routeId"] = data[route]["busRouteId"]
        route_list.append(route_dict)
    return route_list

