import requests
import xmltodict
from dotenv import load_dotenv
import os

load_dotenv()


# 특정 좌표 인근 정류소 데이터 얻기
def get_stn_list(gpsx, gpsy, radius):
    stn_list = []
    if gpsx == 'null':
        stn_list = 'Null'
    else:
        url = f"http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos?" \
              f"serviceKey={os.getenv('key')}&tmX={gpsx}&tmY={gpsy}&radius={radius}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']
        if data is None:
            stn_list = 'Null'
        elif isinstance(data['itemList'], dict):
            stn_dict = {
                'stnId': data['itemList']['stationId'],
                'stnNm': data['itemList']['stationNm'],
                'arsId': data['itemList']['arsId'],
                'gpsX': data['itemList']['gpsX'],
                'gpsY': data['itemList']['gpsY'],
                'dist': data['itemList']['dist']
            }
            stn_list.append(stn_dict)
        else:
            data_list = data['itemList']
            for station in range(len(data_list)):
                stn_dict = {
                    'stnId': data_list[station]['stationId'],
                    'stnNm': data_list[station]['stationNm'],
                    'arsId': data_list[station]['arsId'],
                    'gpsX': data_list[station]['gpsX'],
                    'gpsY': data_list[station]['gpsY'],
                    'dist': data_list[station]['dist']
                }
                stn_list.append(stn_dict)
    return stn_list
