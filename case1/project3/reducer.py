#!/usr/bin/python

import sys

maxValue = 0
oldKey = None

for line in sys.stdin:
  mapped_data = line.strip().split("\t")
  if len(mapped_data) != 2:
    continue

  key, value = mapped_data

  if key and key != oldKey:
    if oldKey != None:
      print oldKey, "\t", maxValue
    oldKey = key
    maxValue = 0

  floatValue = float(value)
  if maxValue < floatValue:
    maxValue = floatValue

if oldKey != None:
  print oldKey, "\t", maxValue
