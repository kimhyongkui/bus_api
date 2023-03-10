import requests
import xmltodict
from dotenv import load_dotenv
from db.get.db_data import get_stn_data
from fastapi import status, HTTPException
import os

load_dotenv()


# 특정 정류소에 도착 예정인 버스들 (stnId, routeId, ord)
def get_arrival_buses(stn_name, stn_id):
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

            if isinstance(data['itemList'], dict):
                for arrive in [data['itemList']]:
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

            elif data is None:
                raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="데이터가 없습니다")

        return arrive_list

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
