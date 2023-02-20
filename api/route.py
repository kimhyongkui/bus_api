import requests
import xmltodict
from dotenv import load_dotenv
import os

load_dotenv()


def get_route_all():
    try:
        url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={os.getenv('key')}"
        content = requests.get(url).content
        dict = xmltodict.parse(content)
        data = dict['ServiceResult']['msgBody']['itemList']
        route_list = []
        for route in data:
            route_dict = {
                "routeNm": route["busRouteNm"],
                "routeAbrv": route["busRouteAbrv"],
                "routeId": route["busRouteId"]
            }
            route_list.append(route_dict)

        return route_list

    except Exception as err:
        return f"{err}"

