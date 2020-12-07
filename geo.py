
import geocoder


class geo_location:
    myloc = geocoder.ip('me')
    loc = myloc.address
    lng = int(myloc.lng * 10 ** 4)
    lat = int(myloc.lat * 10 ** 4)
    ci = myloc.city
    sta = myloc.state

