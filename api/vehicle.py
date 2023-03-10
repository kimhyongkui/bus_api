import requests
import xmltodict
from dotenv import load_dotenv
from api.route import get_all_route_list
from db.get.db_data import get_route_list
from fastapi import status, HTTPException
import os

load_dotenv()


# 특정 노선의 버스 조회
def get_vehicle_data(route_name):
    try:
        route_list = get_route_list(route_name)
        url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?" \
              f"serviceKey={os.getenv('key')}&busRouteId={route_list['routeId']}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']
        vehicle_list = []
        if data:
            if isinstance(data['itemList'], dict):
                vehicle_dict = {
                    'routeId': route_list['routeId'],
                    'vehId': data['itemList']['vehId'],
                    'plainNo': data['itemList']['plainNo'],
                    'gpsX': data['itemList']['gpsX'],
                    'gpsY': data['itemList']['gpsY']
                }
                vehicle_list.append(vehicle_dict)

            elif isinstance(data['itemList'], list):
                for vehicle in data['itemList']:
                    vehicle_dict = {
                        'routeId': route_list['routeId'],
                        'vehId': vehicle['vehId'],
                        'plainNo': vehicle['plainNo'],
                        'gpsX': vehicle['gpsX'],
                        'gpsY': vehicle['gpsY']
                    }
                    vehicle_list.append(vehicle_dict)
        else:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

        return vehicle_list

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


# 전체 노선의 버스 조회
def get_all_vehicle_data():
    try:
        route_list = get_all_route_list()
        vehicle_list = []
        for route_data in route_list:
            data = get_vehicle_data(route_data['routeNm'])
            if data is not None and not isinstance(data, str):
                vehicle_list.append(data)
        return vehicle_list

    except Exception as err:
        return f"{err}, 노선 이름을 확인하세요"
