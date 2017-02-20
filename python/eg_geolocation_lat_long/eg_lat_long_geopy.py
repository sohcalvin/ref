from geopy.distance import vincenty

def distanceBetweenLatLong() :
    newport_ri = (41.49008, -71.312796)
    cleveland_oh = (41.499498, -81.695391)
    print(vincenty(newport_ri, cleveland_oh).miles)
    # 538.3904451566326


from geopy.geocoders import Nominatim
geolocator = Nominatim()
print(geolocator.api)
location = geolocator.geocode("Jurong point Singapore")
# print(location.address)


print((location.latitude, location.longitude))
# (40.7410861, -73.9896297241625)
# >>> print(location.raw)
# {'place_id': '9167009604', 'type': 'attraction', ...}