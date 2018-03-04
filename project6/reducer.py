#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:
  data = line.strip()
  count += 1 if "10.99.99.186" in data else 0

print count
