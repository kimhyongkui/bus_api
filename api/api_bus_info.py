import requests
import xmltodict
from dotenv import load_dotenv
from db.db_get_data import get_stn_data
import os

load_dotenv()
key = os.getenv('key')


# 특정 정류소에 도착 예정인 버스들 (stnId, routeId, ord 사용)
def get_arrive_bus_info(stnNm, stnId):
    result = get_stn_data(stnNm, stnId)
    arrive_list = []

    for result_list in result:
        url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?" \
              f"serviceKey={key}&stId={result_list[4]}&busRouteId={result_list[0]}&ord={result_list[2]}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']

        if data is None:
            print('데이터가 없습니다')

        elif isinstance(data['itemList'], dict):
            data_list = [data['itemList']]

            for arrive in range(len(data_list)):
                arrive_dict = {'routeId': result_list[0],
                               'routeNm': data_list[arrive]['rtNm'],
                               'stnOrd': result_list[2],
                               'stnNm': data_list[arrive]['stNm'],
                               'stnId': result_list[4],
                               'plainNo1': data_list[arrive]['plainNo1'],
                               'arrmsg1': data_list[arrive]['arrmsg1'],
                               'stnNm1': data_list[arrive]['stationNm1'],
                               'plainNo2': data_list[arrive]['plainNo2'],
                               'arrmsg2': data_list[arrive]['arrmsg2'],
                               'stnNm2': data_list[arrive]['stationNm2']
                               }
                arrive_list.append(arrive_dict)

    return arrive_list