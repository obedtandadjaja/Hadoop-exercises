#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:
  data = line.strip()
  count += 1 if "/assets/js/the-associates.js" in data else 0

print count
