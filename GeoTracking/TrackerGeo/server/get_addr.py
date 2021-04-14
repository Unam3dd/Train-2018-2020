#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
import platform
import argparse

try:
    from geopy.geocoders import Nominatim
except ImportError:
    sys.exit("\033[31m[!] Error Geopy Not Found !")


def get_address(latlong):
    geolocator = Nominatim(user_agent="get_address_by_latlong")
    location = geolocator.reverse(latlong)
    return location.address


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('latitude',type=str,help='Latitude')
    parser.add_argument('longitude',type=str, help='Longitude')
    args = parser.parse_args()
    string = "%s,%s" % (args.latitude,args.longitude)
    addr = get_address(string)
    print(addr)