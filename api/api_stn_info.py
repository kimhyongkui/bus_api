from api.api_gps import current_location, geocoding
from api.api_station import get_stn_list


# 특정 지역 좌표 입력해서 인근 정류소 구해보기
def get_station_list(address, rad):
    adr = geocoding(address)
    gps = get_stn_list(adr['gpsX'], adr['gpsY'], rad)
    data_list = []
    for data in range(len(gps)):
        data_dict = {'stnId': gps[data]['stnId'],
                     'stnNm': gps[data]['stnNm'],
                     'arsId': gps[data]['arsId'],
                     'dist': gps[data]['dist']
                     }
        data_list.append(data_dict)

    return data_list


# 현재 좌표 입력해서 인근 정류소 구해보기
def get_cur_stn_list(rad):
    adr = current_location()
    gps = get_stn_list(adr['gpsX'], adr['gpsY'], rad)
    data_list = []
    for data in range(len(gps)):
        data_dict = {'stnId': gps[data]['stnId'],
                     'stnNm': gps[data]['stnNm'],
                     'arsId': gps[data]['arsId'],
                     'dist': gps[data]['dist']
                     }
        data_list.append(data_dict)

    return data_list
