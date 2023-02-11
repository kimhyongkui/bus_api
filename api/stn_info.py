from api.gps import current_location, specific_location
from api.search_station import get_stn_list


# 특정 지역 좌표 입력해서 인근 정류소 구해보기
def get_station_list(address, rad):
    adr = specific_location(address)
    gps = get_stn_list(adr['gpsX'], adr['gpsY'], rad)
    data_list = []
    if gps == ['Null']:
        data_list = 'Null'
    else:
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
    if gps == ['Null']:
        data_list = 'Null'
    else:
        for data in range(len(gps)):
            data_dict = {'stnId': gps[data]['stnId'],
                         'stnNm': gps[data]['stnNm'],
                         'arsId': gps[data]['arsId'],
                         'dist': gps[data]['dist']
                         }
            data_list.append(data_dict)
    return data_list

