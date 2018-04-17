#!/usr/bin/env python
#
# John Van Note
# 04.08.2018
#

import json

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
        #print stop
        stops.append(stop)
    return stops


def json_object_to_septa(json_object):
    lat = json_object[KEY_LAT]
    lng = json_object[KEY_LNG]
    stop_id = json_object[KEY_STOP_ID]
    stop_name = json_object[KEY_STOP_NAME]
    return SeptaStop(lat, lng, stop_id, stop_name)


def main():
    stop = SeptaStop(-75.20797, 40.076831, 250, "Germantown Av & Bethlehem Pk - FS")
    print stop.stop_name
    print stop.stop_id

    if DEBUG:
        with open(TEST_FILE, 'r') as json_data_file:
            data = json_data_file.read()

    septa_data = parse_septa_json(data)
    print septa_data
    stops = json_array_to_septa(septa_data)
    print stops



if __name__ == "__main__":
    main()
