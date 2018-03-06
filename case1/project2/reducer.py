#!/usr/bin/python

import sys

tot_sales = 0
prev_category = None

for line in sys.stdin:
  data_mapped = line.strip().split("\t")

  # remove error data if any, field length < 2
  if len(data_mapped) != 2:
    continue

  current_category, sales = data_mapped

  if prev_category and prev_category != current_category:
    print prev_category, "\t", tot_sales
    prev_category = current_category;
    tot_sales = 0

  prev_category = current_category
  tot_sales += float(sales)

if prev_category != None:
  print prev_category, "\t", tot_sales
