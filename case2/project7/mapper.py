#!/usr/bin/python

import sys

for line in sys.stdin:
  data = line.strip().split(" ")

  ip = data[0]
  identity = data[1]
  username = data[2]
  time = data[3] + " " + data[4]

  request = data[6]
  request = request.replace("http://www.the-associates.co.uk", "")

  status = data[8]
  size = data[9]

  # identity: nullable -> "-"
  # username: nullable -> "-"
  # time: format -> [day/month/year:hour:minute:second zone]
  # status: 200(OK), 304(not modified), 404(not found)
  # size: returns "-" if status is 304

  if len(request) > 1 and request.find(".php") == -1 and request.find(".") != -1:
    print request
