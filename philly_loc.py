#/usr/bin/env python
#
# Kurt Schmidt
# 4/2015
#
# EDITOR:  tabstop=2, cols=80
#

import random
import math

min_lat = 39.9155802878
max_lat = 40.1026872756
min_long = -75.2388309423
max_long = -74.9699425597

lat_delta = max_lat - min_lat
long_delta = max_long - min_long

multiple = 1000


def getLoc() :
  '''Returns some location in Phila. ( LAT, LONG ), in decimal degrees'''

  x = random.randint(0, int(long_delta*multiple))
  y = random.randint(0, int(lat_delta*multiple))

  return min_lat + y/float(multiple) , min_long + x/float(multiple)