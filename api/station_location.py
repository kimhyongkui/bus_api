from api.gps import current_location, specific_location
from api.search_station import search_station
from fastapi import status, HTTPException


# 특정 지역 좌표 입력해서 인근 정류소 구해보기
def get_spe_stn_list(address, rad):
    try:
        address = specific_location(address)
        gps = search_station(address['gpsX'], address['gpsY'], rad)
        stn_list = []
        for stn_data in gps:
            stn_dict = {
                'stnId': stn_data['stnId'],
                'stnNm': stn_data['stnNm'],
                'arsId': stn_data['arsId'],
                'dist': stn_data['dist']
            }
            stn_list.append(stn_dict)

        return stn_list

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))


# 현재 좌표 입력해서 인근 정류소 구해보기
def get_cur_stn_list(rad):
    try:
        address = current_location()
        gps = search_station(address['gpsX'], address['gpsY'], rad)
        stn_list = []
        for stn_data in gps:
            stn_dict = {
                'stnId': stn_data['stnId'],
                'stnNm': stn_data['stnNm'],
                'arsId': stn_data['arsId'],
                'dist': stn_data['dist']
            }
            stn_list.append(stn_dict)

        return stn_list

    except HTTPException:
        raise

    except TimeoutError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="geoplugin 접속 오류")

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
