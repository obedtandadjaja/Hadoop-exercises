#!/usr/bin/python

import sys

count = 0
totalValue = 0

for line in sys.stdin:
  data = line.strip()

  totalValue += float(value)
  count += 1

print totalValue, "\t", count
