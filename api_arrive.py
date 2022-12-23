import requests, xmltodict
from dotenv import load_dotenv
import os
from api_bus import get_bus_all


load_dotenv()
key = os.getenv('key')

# 특정 경유노선의 전체정류소 데이터 얻기
def get_arrive(busid):
    url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?serviceKey={key}&busRouteId={busid}"
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    data = dict['ServiceResult']['msgBody']['itemList']
    arrive_list = []
    for arrive in range(len(data)):
        arrive_dict = {}
        arrive_id = busid
        arrive_busnm = data[arrive]['rtNm']
        arrive_ord = data[arrive]['staOrd']
        arrive_stnm = data[arrive]['stNm']
        arrive_stid = data[arrive]['stId']

        arrive_dict['bus_id'] = arrive_id
        arrive_dict['rtNm'] = arrive_busnm
        arrive_dict['staOrd'] = arrive_ord
        arrive_dict['stNm'] = arrive_stnm
        arrive_dict['stId'] = arrive_stid
        arrive_list.append(arrive_dict)
        print(arrive_dict)
    return arrive_list

get_arrive(100100081)

# 모든 경유노선의 전체정류소 데이터 얻기
def get_arrive_all():
    bus_list = get_bus_all()
    arrive_list = []
    for bus in bus_list:
        busid = bus['bus_id']
        url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?serviceKey={key}&busRouteId={busid}"
        content = requests.get(url).content
        dict = xmltodict.parse(content)
        data = dict['ServiceResult']['msgBody']['itemList']
        for arrive in range(len(data)) :
            arrive_dict = {}
            arrive_id = busid
            arrive_busnm = data[arrive]['rtNm']
            arrive_ord = data[arrive]['staOrd']
            arrive_stnm = data[arrive]['stNm']
            arrive_stid = data[arrive]['stId']

            arrive_dict['bus_id'] = arrive_id
            arrive_dict['rtNm'] = arrive_busnm
            arrive_dict['staOrd'] = arrive_ord
            arrive_dict['stNm'] = arrive_stnm
            arrive_dict['stId'] = arrive_stid
            arrive_list.append(arrive_dict)
            print(arrive_dict)
    return arrive_list


# 한 정류소의 특정노선의 도착예정 정보 조회 stId / busRouteId / ord
def get_arrive_info(stId, busid, ord):
    url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?serviceKey={key}&stId={stId}&busRouteId={busid}&ord={ord}"
    content = requests.get(url).content
    xmldict = xmltodict.parse(content)
    data = xmldict['ServiceResult']['msgBody']
    print(type(data['itemList']))
    # arr = arrive
    arr_list = []
    arr_id = busid
    arr_ord = ord

    if data is None:
        print('데이터가 없습니다')

    elif isinstance(data['itemList'], dict):
        data_list = []
        data_list.append(data['itemList'])

        for arr in range(len(data_list)):
            arr_dict = {}
            arr_busnm = data_list[arr]['rtNm']
            arr_stnm = data_list[arr]['stNm']
            arr_stid = data_list[arr]['stId']
            arr_No1 = data_list[arr]['plainNo1']
            arr_msg1 = data_list[arr]['arrmsg1']
            arr_stnm1 = data_list[arr]['stationNm1']
            arr_No2 = data_list[arr]['plainNo2']
            arr_msg2 = data_list[arr]['arrmsg2']
            arr_stnm2 = data_list[arr]['stationNm2']

            arr_dict['bus_id'] = arr_id
            arr_dict['rtNm'] = arr_busnm
            arr_dict['staOrd'] = arr_ord
            arr_dict['stNm'] = arr_stnm
            arr_dict['stId'] = arr_stid
            arr_dict['plainNo1'] = arr_No1
            arr_dict['arrmsg1'] = arr_msg1
            arr_dict['stationNm1'] = arr_stnm1
            arr_dict['plainNo2'] = arr_No2
            arr_dict['arrmsg2'] = arr_msg2
            arr_dict['stationNm2'] = arr_stnm2
            arr_list.append(arr_dict)
            print(f"노선ID : {arr_id},"
                  f" 노선이름 : {arr_busnm},"
                  f" 노선순번 : {arr_ord},"
                  f" 정류소이름 : {arr_stnm},"
                  f" 노선ID : {arr_stid},"
                  f" 첫번째 도착예정버스 : {arr_No1},"
                  f" 현재 정류장 : {arr_stnm1},"
                  f" 도착예정시간 : {arr_msg1},"
                  f" 첫번째 도착예정버스 : {arr_No2},"
                  f" 도착예정시간 : {arr_msg2},"
                  f" 현재 정류장 : {arr_stnm2}"
                  , sep='\n')

    return arr_list

get_arrive_info(120000041, 100100081, 99)


