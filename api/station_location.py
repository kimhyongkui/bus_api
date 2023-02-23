from api.gps import current_location, specific_location
from api.search_station import search_station


# 특정 지역 좌표 입력해서 인근 정류소 구해보기
def get_spe_stn_list(address, rad):
    try:
        address = specific_location(address)
        gps = search_station(address['gpsX'], address['gpsY'], rad)
        stn_list = []
        if gps == 'Null':
            stn_list = '지명과 거리를 확인하세요'

        else:
            for stn_data in gps:
                stn_dict = {
                    'stnId': stn_data['stnId'],
                    'stnNm': stn_data['stnNm'],
                    'arsId': stn_data['arsId'],
                    'dist': stn_data['dist']
                }
                stn_list.append(stn_dict)

        return stn_list

    except Exception as err:
        return f"{err}, 에러 발생"


# 현재 좌표 입력해서 인근 정류소 구해보기
def get_cur_stn_list(rad):
    try:
        address = current_location()
        gps = search_station(address['gpsX'], address['gpsY'], rad)
        stn_list = []
        if gps == 'Null':
            stn_list = '주변에 정류소가 없습니다'

        else:
            for stn_data in gps:
                stn_dict = {
                    'stnId': stn_data['stnId'],
                    'stnNm': stn_data['stnNm'],
                    'arsId': stn_data['arsId'],
                    'dist': stn_data['dist']
                }
                stn_list.append(stn_dict)

        return stn_list

    except Exception as err:
        return f"{err}, 에러 발생"
