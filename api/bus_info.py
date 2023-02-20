import requests
import xmltodict
from dotenv import load_dotenv
from db.get.db_data import get_stn_data
import os

load_dotenv()


# 특정 정류소에 도착 예정인 버스들 (stnId, routeId, ord 사용)
def get_arrive_bus_info(stnNm, stnId):
    try:
        result = get_stn_data(stnNm, stnId)
        arrive_list = []
        for result_list in result:
            url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?" \
                  f"serviceKey={os.getenv('key')}" \
                  f"&stId={result_list['stnId']}" \
                  f"&busRouteId={result_list['routeId']}" \
                  f"&ord={result_list['stnOrd']}"
            content = requests.get(url).content
            xmldict = xmltodict.parse(content)
            data = xmldict['ServiceResult']['msgBody']
            if data is None:
                arrive_list = '데이터가 없습니다'

            elif isinstance(data['itemList'], dict):
                data_list = [data['itemList']]
                for arrive in data_list:
                    arrive_dict = {
                        'routeId': result_list['routeId'],
                        'routeNm': arrive['rtNm'],
                        'stnOrd': result_list['stnOrd'],
                        'stnNm': arrive['stNm'],
                        'stnId': result_list['stnId'],
                        'plainNo1': arrive['plainNo1'],
                        'arrmsg1': arrive['arrmsg1'],
                        'stnNm1': arrive['stationNm1'],
                        'plainNo2': arrive['plainNo2'],
                        'arrmsg2': arrive['arrmsg2'],
                        'stnNm2': arrive['stationNm2']
                    }
                    arrive_list.append(arrive_dict)

        return arrive_list

    except Exception as err:
        return f"{err}, 정류소 이름 또는 ID를 확인하세요"

