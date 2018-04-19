#!/usr/bin/env python
#
# John Van Note
# 04.08.2018
#

import json
import sys

from math import hypot
from SeptaStop import *

DEBUG = True
TEST_FILE = "test_data.json"
KEY_LAT = "lat"
KEY_LNG = "lng"
KEY_STOP_ID = "stopid"
KEY_STOP_NAME = "stopname"


def parse_septa_json(json_str):
    septa_data = json.loads(json_str)
    return septa_data

def json_array_to_septa(json_array):
    stops = []
    for stop in json_array:
        stops.append(json_object_to_septa(stop))
    return stops


def json_object_to_septa(json_object):
    lat = float(json_object[KEY_LAT])
    lng = float(json_object[KEY_LNG])
    stop_id = json_object[KEY_STOP_ID]
    stop_name = json_object[KEY_STOP_NAME]
    return SeptaStop(lat, lng, stop_id, stop_name)


def find_distance(x1, x2, y1, y2):
    return hypot(x2 - x1, y2 - y1)


def main(argv):
    print sys.argv[1]
    print sys.argv[2]
    print sys.argv[3]

    if (len(argv) < 4):
        raise BaseException("Invalid number of arguments")

    lng = float(argv[1])
    lat = float(argv[2])
    num = int(argv[3])

    if DEBUG:
        with open(TEST_FILE, 'r') as json_data_file:
            data = json_data_file.read()

    septa_data = parse_septa_json(data)
    stops = json_array_to_septa(septa_data)

    stop_dict = {}
    for stop in stops:
        stop_dict[stop] = find_distance(lng, stop.lng, lat, stop.lat)

    i = 0
    for key, value in sorted(stop_dict.iteritems(), key=lambda (k,v): (v,k)):
        if num <= i:
            break
        print key
        print value
        i += 1

if __name__ == "__main__":
    main(sys.argv)
