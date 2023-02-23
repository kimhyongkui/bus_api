from api.gps import current_location, specific_location
from api.search_station import get_stn_list


# 특정 지역 좌표 입력해서 인근 정류소 구해보기
def get_station_list(address, rad):
    try:
        adr = specific_location(address)
        gps = get_stn_list(adr['gpsX'], adr['gpsY'], rad)
        data_list = []
        if gps == 'Null':
            data_list = '지명과 거리를 확인하세요'

        else:
            for data in gps:
                data_dict = {
                    'stnId': data['stnId'],
                    'stnNm': data['stnNm'],
                    'arsId': data['arsId'],
                    'dist': data['dist']
                }
                data_list.append(data_dict)

        return data_list

    except Exception as err:
        return f"{err}, 에러 발생"

# 현재 좌표 입력해서 인근 정류소 구해보기
def get_cur_stn_list(rad):
    try:
        adr = current_location()
        gps = get_stn_list(adr['gpsX'], adr['gpsY'], rad)
        data_list = []
        if gps == 'Null':
            data_list = '주변에 정류소가 없습니다'

        else:
            for data in gps:
                data_dict = {
                    'stnId': data['stnId'],
                    'stnNm': data['stnNm'],
                    'arsId': data['arsId'],
                    'dist': data['dist']
                }
                data_list.append(data_dict)

        return data_list

    except Exception as err:
        return f"{err}, 에러 발생"


# def stn_list(address=None, *, rad):
#     if address:
#         adr = specific_location(address)
#     else:
#         adr = current_location()
#     try:
#         gps = get_stn_list(adr['gpsX'], adr['gpsY'], rad)
#         data_list = []
#
#         if gps == 'Null':
#             data_list = '주변에 정류소가 없습니다'
#
#         else:
#             for data in gps:
#                 data_dict = {
#                     'stnId': data['stnId'],
#                     'stnNm': data['stnNm'],
#                     'arsId': data['arsId'],
#                     'dist': data['dist']
#                 }
#                 data_list.append(data_dict)
#
#         return data_list
#
#     except Exception as err:
#         return f"{err}, 에러 발생"