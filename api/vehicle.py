import requests
import xmltodict
from dotenv import load_dotenv
from db.get.db_data import get_route_list
from fastapi import status, HTTPException
import os

load_dotenv()


# 특정 노선의 버스 조회
def get_vehicle_data(route_name):
    try:
        route_list = get_route_list(route_name)
        url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?" \
              f"serviceKey={os.getenv('KEY')}&busRouteId={route_list['routeId']}"
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
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="데이터가 없습니다")

        return vehicle_list

    except HTTPException:
        raise
    except requests.exceptions.ConnectTimeout:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='외부 api 문제')
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


# 모든 버스 조회
def get_all_vehicle_data():
    vehicle_list = []
    for route_data in get_route_list():
        try:
            data = get_vehicle_data(route_data['routeNm'])
            vehicle_list.extend(data)
            print(route_data['routeId'])

        except HTTPException as err:
            print(f"{route_data['routeId']}:{err.detail}")
            continue

    return vehicle_list
