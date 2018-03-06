#!/usr/bin/python

import sys

maxCount = 0
maxData = None

count = 0
oldData = None

for line in sys.stdin:
  data = line.strip()
  if data and data != oldData:
    if oldData != None and count > maxCount:
      maxCount = count
      maxData = oldData
    oldData = data
    count = 0

  count += 1

if oldData != None and count > maxCount:
  maxCount = count
  maxData = oldData

print maxData, "\t", maxCount
