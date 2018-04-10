#!/usr/bin/env python
#
# John Van Note
# 04.08.2016
#

class SeptaStop:

  def __init__ (self, lng, lat, stop_id, stop_name):
    self.lng = lng
    self.lat = lat
    self.stop_id = stop_id
    self.stop_name = stop_name

  @property
  def lng(self):
    return self._lng

  @lng.setter
  def lng(self, lng):
    self._lng = lng

  @property
  def lat(self):
    return self._lat

  @lat.setter
  def lat(self, lat):
    self._lat = lat

  @property
  def stop_id(self):
    print "Here"
    return self._stop_id

  @stop_id.setter
  def stop_id(self, stop_id):
    print "There"
    self._stop_id = stop_id

  @property
  def stop_name(self):
    return  self._stop_name

  @stop_name.setter
  def stop_name(self, stop_name):
    self._stop_name = stop_name