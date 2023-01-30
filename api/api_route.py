import requests
import xmltodict
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')





def get_route_all():
    url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={key}"
    content = requests.get(url).content  # GET요청
    dict = xmltodict.parse(content)  # XML을 dictionary로 파싱
    data = dict['ServiceResult']['msgBody']['itemList']

    route_list = []
    for route in range(len(data)):
        route_dict = {}
        route_dict["routeNm"] = data[route]["busRouteNm"]  # 버스 노선 이름
        route_dict["routeAbrv"] = data[route]["busRouteAbrv"]  # 버스 노선 이름
        route_dict["routeId"] = data[route]["busRouteId"]  # 버스 노선 id
        route_list.append(route_dict)
    return route_list



