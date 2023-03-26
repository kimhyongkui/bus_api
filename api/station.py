import requests
import xmltodict
from dotenv import load_dotenv
import os
from db.get.db_data import get_route_list
from fastapi import status, HTTPException

load_dotenv()


# 특정 노선의 경유 정류소 데이터 얻기
def get_station_data(route_id):
    try:
        url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?" \
              f"serviceKey={os.getenv('KEY')}&busRouteId={route_id}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']
        stn_list = []
        if data:
            for station in data['itemList']:
                stn_dict = {
                    'routeId': route_id,
                    'routeNm': station['busRouteNm'],
                    'routeAbrv': station['busRouteAbrv'],
                    'stnId': station['station'],
                    'stnNm': station['stationNm'],
                    'arsId': station['arsId'],
                    'direction': station['direction'],
                    'gpsX': station['gpsX'],
                    'gpsY': station['gpsY']
                }
                stn_list.append(stn_dict)

        else:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="데이터가 없습니다")

        return stn_list

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


# 모든 정류소 데이터 얻기
def get_all_station_data():
    stn_data_list = []
    for route_id in get_route_list():
        try:
            data = get_station_data(route_id['routeId'])
            stn_data_list.extend(data)
            print(route_id['routeId'])

        except HTTPException as err:
            print(f"{route_id['routeId']}:{err.detail}")
            continue

    return stn_data_list
