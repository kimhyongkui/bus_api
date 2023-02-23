import requests
import xmltodict
from dotenv import load_dotenv
import os

load_dotenv()


# 특정 좌표 인근 정류소 데이터 얻기
def get_stn_list(gpsx, gpsy, radius):
    try:
        stn_list = []
        url = f"http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos?" \
              f"serviceKey={os.getenv('key')}&tmX={gpsx}&tmY={gpsy}&radius={radius}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']['itemList']
        if isinstance(data, dict):
            stn_dict = {
                'stnId': data['stationId'],
                'stnNm': data['stationNm'],
                'arsId': data['arsId'],
                'gpsX': data['gpsX'],
                'gpsY': data['gpsY'],
                'dist': data['dist']
            }
            stn_list.append(stn_dict)
        else:
            for station in data:
                stn_dict = {
                    'stnId': station['stationId'],
                    'stnNm': station['stationNm'],
                    'arsId': station['arsId'],
                    'gpsX': station['gpsX'],
                    'gpsY': station['gpsY'],
                    'dist': station['dist']
                }
                stn_list.append(stn_dict)

        return stn_list
    # 매개변수 값이 잘못되었거나 data의 값이 없을때
    except TypeError as err:
        return 'Null'
    except Exception as err:
        return err
