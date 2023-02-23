import requests
import xmltodict
from dotenv import load_dotenv
from db.get.db_data import get_stn_data
import os

load_dotenv()


# 특정 정류소에 도착 예정인 버스들 (stnId, routeId, ord 사용)
def get_arrive_bus_info(stn_name, stn_id):
    try:
        stn_data = get_stn_data(stn_name, stn_id)
        arrive_list = []
        for station in stn_data:
            url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?" \
                  f"serviceKey={os.getenv('key')}" \
                  f"&stId={station['stnId']}" \
                  f"&busRouteId={station['routeId']}" \
                  f"&ord={station['stnOrd']}"
            content = requests.get(url).content
            xmldict = xmltodict.parse(content)
            data = xmldict['ServiceResult']['msgBody']
            if data is None:
                arrive_list = '데이터가 없습니다'

            elif isinstance(data['itemList'], dict):
                # data['itemList']가 리스트로 묶여 있지 않으면 에러 발생
                data_list = [data['itemList']]
                for arrive in data_list:
                    arrive_dict = {
                        'routeId': station['routeId'],
                        'routeNm': arrive['rtNm'],
                        'stnOrd': station['stnOrd'],
                        'stnNm': arrive['stNm'],
                        'stnId': station['stnId'],
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
