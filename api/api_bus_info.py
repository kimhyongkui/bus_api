import requests
import xmltodict
from dotenv import load_dotenv
from db.db_get_data import get_data
import os


load_dotenv()
key = os.getenv('key')


# 특정 정류소에 도착 예정인 버스들 (stnId, routeId, ord 사용)
def get_arrive_bus_info(stnNm, stnId):
    result = get_data(stnNm, stnId)
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
            data_list = []
            data_list.append(data['itemList'])

            for arrive in range(len(data_list)):
                arrive_dict = {}

                arrive_dict['routeId'] = result_list[0]  # 노선ID
                arrive_dict['routeNm'] = data_list[arrive]['rtNm']  # 노선이름
                arrive_dict['stnOrd'] = result_list[2]  # 노선순번
                arrive_dict['stnNm'] = data_list[arrive]['stNm']  # 정류소이름
                arrive_dict['stnId'] = result_list[4]  # 정류소ID
                arrive_dict['plainNo1'] = data_list[arrive]['plainNo1']  # 첫번째 도착예정버스
                arrive_dict['arrmsg1'] = data_list[arrive]['arrmsg1']  # 도착예정시간
                arrive_dict['stnNm1'] = data_list[arrive]['stationNm1']  # 현재 정류장
                arrive_dict['plainNo2'] = data_list[arrive]['plainNo2']  # 두번째 도착예정버스
                arrive_dict['arrmsg2'] = data_list[arrive]['arrmsg2']  # 도착예정시간
                arrive_dict['stnNm2'] = data_list[arrive]['stationNm2']  # 현재 정류장

                arrive_list.append(arrive_dict)

    return arrive_list

print(get_arrive_bus_info('명동입구', 101000148))