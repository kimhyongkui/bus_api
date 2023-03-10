import requests
import xmltodict
from dotenv import load_dotenv
from fastapi import status, HTTPException
import os

load_dotenv()


def get_all_route_list():
    try:
        url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={os.getenv('key')}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']['itemList']
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
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{err}")
