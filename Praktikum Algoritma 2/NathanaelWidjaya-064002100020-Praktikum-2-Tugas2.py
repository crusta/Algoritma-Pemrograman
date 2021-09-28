from math import *
def haversine(lon1, lat1, lon2, lat2):
    """
    menghitung dua jarak menggunakan lattitude dan longitude.
    """
    # mengubah desimal ke radian
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius bumi dalam kilometer.
    return c * r


a1 = float(input("Masukan lattitude 1 :"))
a2 = float(input("masukan lattitude 2 :"))
b1 = float(input("masukan Longitude 1 :"))
b2 = float(input("masukan longitude 2 :"))
center_point = [{'lat': a1, 'lng': b1}]
test_point = [{'lat': a2, 'lng': b2}]

lat1 = center_point[0]['lat']
lon1 = center_point[0]['lng']
lat2 = test_point[0]['lat']
lon2 = test_point[0]['lng']

a = haversine(lon1, lat1, lon2, lat2)

print('Distance (km) : ', a ,"km")
