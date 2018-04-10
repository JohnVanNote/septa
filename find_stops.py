#!/usr/bin/env python
#
# John Van Note
# 04.08.2018
#

from SeptaStop import *

def main():
  stop = SeptaStop(-75.20797, 40.076831, 250, "Germantown Av & Bethlehem Pk - FS")
  print stop.stop_name
  print stop.stop_id

if __name__ == "__main__":
  main()
