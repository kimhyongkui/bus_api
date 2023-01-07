import requests
import xmltodict
from dotenv import load_dotenv
import os
from pymysql_crud import conn

load_dotenv()
key = os.getenv('key')


# 특정 정류소에 도착 예정인 버스들 (stnId, routeId, ord 이용)
def get_arrive_bus_info1(value1, value2):
    curs = conn.cursor()
    sql = f"SELECT * FROM arrive WHERE stnNm='{value1}' AND stnId={value2}"
    curs.execute(sql)
    result = curs.fetchall()

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

                arrive_dict['routeId'] = result_list[0]
                arrive_dict['routeNm'] = data_list[arrive]['rtNm']
                arrive_dict['stnOrd'] = result_list[2]
                arrive_dict['stnNm'] = data_list[arrive]['stNm']
                arrive_dict['stnId'] = result_list[4]
                arrive_dict['plainNo1'] = data_list[arrive]['plainNo1']
                arrive_dict['arrmsg1'] = data_list[arrive]['arrmsg1']
                arrive_dict['stnNm1'] = data_list[arrive]['stationNm1']
                arrive_dict['plainNo2'] = data_list[arrive]['plainNo2']
                arrive_dict['arrmsg2'] = data_list[arrive]['arrmsg2']
                arrive_dict['stnNm2'] = data_list[arrive]['stationNm2']

                arrive_list.append(arrive_dict)
                print(f"노선ID : {arrive_dict['routeId']},"
                      f" 노선이름 : {arrive_dict['routeNm']},"
                      f" 노선순번 : {arrive_dict['stnOrd']},"
                      f" 정류소이름 : {arrive_dict['stnNm']},"
                      f" 정류소ID : {arrive_dict['stnId']},"
                      f" 첫번째 도착예정버스 : {arrive_dict['plainNo1']},"
                      f" 도착예정시간 : {arrive_dict['arrmsg1']},"
                      f" 현재 정류장 : {arrive_dict['stnNm1']},"
                      f" 두번째 도착예정버스 : {arrive_dict['plainNo2']},"
                      f" 도착예정시간 : {arrive_dict['arrmsg2']},"
                      f" 현재 정류장 : {arrive_dict['stnNm2']}")
    conn.close()
    return arrive_list

get_arrive_bus_info('을지로5가', 101000066)

# 특정 정류소에 도착 예정인 버스들 (stnId, routeId, ord 이용)
def get_arrive_bus_info2(arsId):
    url = f"http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid?serviceKey={key}&arsId={arsId}"
    content = requests.get(url).content
    xmldict = xmltodict.parse(content)
    data = xmldict['ServiceResult']['msgBody']

    arrive_list = []

    conn.close()
    return arrive_list