import requests
import xmltodict
from dotenv import load_dotenv
import os
from api_route import get_route_all
from pymysql_crud import conn

load_dotenv()
key = os.getenv('key')


# 특정 경유노선의 전체정류소 데이터 얻기
def get_arrive(routeid):
    url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?" \
          f"serviceKey={key}&busRouteId={routeid}"
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    data = dict['ServiceResult']['msgBody']['itemList']
    arrive_list = []
    for arrive in range(len(data)):
        arrive_dict = {}
        arrive_dict['routeId'] = routeid  # 노선 ID
        arrive_dict['routeNm'] = data[arrive]['rtNm']  # 노선명
        arrive_dict['stnOrd'] = data[arrive]['staOrd']  # 정류소 순번
        arrive_dict['stnNm'] = data[arrive]['stNm']  # 정류소 이름
        arrive_dict['stnId'] = data[arrive]['stId']  # 정류소 ID

        arrive_list.append(arrive_dict)
        print(arrive_dict)
    return arrive_list



# 모든 경유노선의 전체정류소 데이터 얻기
def get_arrive_all():
    route_list = get_route_all()
    arrive_list = []
    for route in route_list:
        routeid = route['routeId']
        url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?" \
              f"serviceKey={key}&busRouteId={routeid}"
        content = requests.get(url).content
        dict = xmltodict.parse(content)
        data = dict['ServiceResult']['msgBody']['itemList']
        for arrive in range(len(data)):
            arrive_dict = {}
            arrive_dict['routeId'] = routeid
            arrive_dict['routeNm'] = data[arrive]['rtNm']
            arrive_dict['stnOrd'] = data[arrive]['staOrd']
            arrive_dict['stnNm'] = data[arrive]['stNm']
            arrive_dict['stnId'] = data[arrive]['stId']

            arrive_list.append(arrive_dict)
            print(arrive_dict)
    return arrive_list




# 한 정류소의 특정노선의 도착예정 정보 조회 stnId / busRouteId / ord
def get_arrive_info(stnId, routeid, ord):
    url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?" \
          f"serviceKey={key}&stId={stnId}&busRouteId={routeid}&ord={ord}"
    content = requests.get(url).content
    xmldict = xmltodict.parse(content)
    data = xmldict['ServiceResult']['msgBody']

    arrive_list = []
    arrive_rtId = routeid
    arrive_ord = ord

    if data is None:
        print('데이터가 없습니다')

    elif isinstance(data['itemList'], dict):
        data_list = []
        data_list.append(data['itemList'])

        for arrive in range(len(data_list)):
            arrive_dict = {}

            arrive_dict['routeId'] = arrive_rtId
            arrive_dict['routeNm'] = data_list[arrive]['rtNm']
            arrive_dict['stnOrd'] = arrive_ord
            arrive_dict['stnNm'] = data_list[arrive]['stNm']
            arrive_dict['stnId'] = data_list[arrive]['stId']
            arrive_dict['plainNo1'] = data_list[arrive]['plainNo1']
            arrive_dict['arrmsg1'] = data_list[arrive]['arrmsg1']
            arrive_dict['stnNm1'] = data_list[arrive]['stationNm1']
            arrive_dict['plainNo2'] = data_list[arrive]['plainNo2']
            arrive_dict['arrmsg2'] = data_list[arrive]['arrmsg2']
            arrive_dict['stnNm2'] = data_list[arrive]['stationNm2']

            arrive_list.append(arrive_dict)
            print(f"노선ID : {arrive_rtId},"
                  f" 노선이름 : {arrive_dict['routeNm']},"
                  f" 노선순번 : {arrive_ord},"
                  f" 정류소이름 : {arrive_dict['stnNm']},"
                  f" 정류소ID : {arrive_dict['stnId']},"
                  f" 첫번째 도착예정버스 : {arrive_dict['plainNo1']},"
                  f" 도착예정시간 : {arrive_dict['arrmsg1']},"
                  f" 현재 정류장 : {arrive_dict['stnNm1']},"
                  f" 두번째 도착예정버스 : {arrive_dict['plainNo2']},"
                  f" 도착예정시간 : {arrive_dict['arrmsg2']},"
                  f" 현재 정류장 : {arrive_dict['stnNm2']}")

    return arrive_list




