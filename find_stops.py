#!/usr/bin/env python
#
# John Van Note
# 04.08.2018
#

import json
import sys
import urllib

from HTMLParser import HTMLParser
from math import hypot
from SeptaStop import *

DEBUG = False
TEST_FILE = "test_data.json"
URL = "http://www3.septa.org/hackathon/Stops/?req1=23"

def read_doc(url):
    '''Reads a webpage document

    Args:
        url (str): The URL to read_doc

    Returns:
        str: The webpage text
    '''
    sock = urllib.urlopen(url)
    doc = sock.read()
    sock.close()
    return doc

def load_json(json_str):
    '''Loads JSON str into a JSON Object/Array for parsing

    Args:
        json_str (str): The JSON String

    Returns:
        list: The JSON string parsed into a list of dictionary's
    '''
    septa_data = json.loads(json_str)
    return septa_data

def json_array_to_septa(json_array):
    '''Converts a JSON Array into a list of SeptaStop's

    Args:
        json_array (list): The JSON list of dictionary's

    Returns:
        list: The list of SeptaStop's
    '''

    stops = []
    for stop in json_array:
        stops.append(json_object_to_septa(stop))
    return stops

def json_object_to_septa(json_object):
    '''Converts a JSON Object into a SeptaStop

    Args:
        json_object (dict): The JSON Object dictionary

    Returns:
        SeptaStop: A converted SeptaStop
    '''

    lat = float(json_object["lat"])
    lng = float(json_object["lng"])
    stop_id = int(json_object["stopid"])
    stop_name = HTMLParser().unescape(json_object["stopname"])
    return SeptaStop(lat, lng, stop_id, stop_name)

def find_distance(x1, x2, y1, y2):
    '''Finds the distance between two points

    Args:
        x1 (float): The x-value of the first point
        x2 (float): The x-value of the second point
        y1 (float): The y-value of the first point
        y2 (float): The y-value of the second point

    Returns:
        float: The distance between (x1,y1) and (x2,y2)
    '''
    return hypot(x2 - x1, y2 - y1)

def main(argv):
    '''Main function

    Args:
        argv(str[]): The program arguments
    '''

    if (len(argv) < 4):
        raise BaseException("Invalid number of arguments")

    lng = float(argv[1])
    lat = float(argv[2])
    num = int(argv[3])

    if DEBUG:
        with open(TEST_FILE, 'r') as json_data_file:
            data = json_data_file.read()
    else:
        data = read_doc(URL)

    septa_data = load_json(data)
    stops = json_array_to_septa(septa_data)

    stop_dict = {}
    for stop in stops:
        stop_dict[stop] = find_distance(lng, stop.lng, lat, stop.lat)

    i = 0
    for key, value in sorted(stop_dict.iteritems(), key=lambda (k,v): (v,k)):
        if num <= i:
            break
        print str(value) \
         + " " + key.stop_name \
         + " (" + str(key.lat) \
         + ", " + str(key.lng) + ")"
        i += 1

if __name__ == "__main__":
    main(sys.argv)
