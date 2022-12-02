import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyAta6tpL9AEHG-1j0WmtedhGIME_8v_Kg0')


geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')


reverse_geocode_result = gmaps.reverse_geocode((126.799875, 37.577504), language='ko')



now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)


addressvalidation_result = gmaps.addressvalidation(['1600 Amphitheatre Pk'],
                                                   regionCode='US',
                                                   locality='Mountain View',
                                                   enableUspsCass=True)

