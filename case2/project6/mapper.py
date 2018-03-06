#!/usr/bin/python

import sys

for line in sys.stdin:
  data = line.strip().split(" ")

  ip = data[0]
  identity = data[1]
  username = data[2]
  time = data[3] + " " + data[4]

  request = data[5]
  curr_index = 6
  for i in xrange(curr_index, len(data)):
    request += " " + data[i]
    curr_index += 1
    if "\"" in data[i]: break

  status = data[curr_index]
  size = data[curr_index+1]

  # identity: nullable -> "-"
  # username: nullable -> "-"
  # time: format -> [day/month/year:hour:minute:second zone]
  # status: 200(OK), 304(not modified), 404(not found)
  # size: returns "-" if status is 304

  print ip
