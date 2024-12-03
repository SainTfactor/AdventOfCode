#!/usr/bin/env python3

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [[int(j) for j in i.split(" ")] for i in f.readlines()]

  return data

data = parse_puzzle_input()
#data = parse_puzzle_input(True)

def is_good_value(value, start, direction):
    diff = value - start
    new_direction = abs(diff) == diff

    if abs(diff) > 3 or abs(diff) < 1:
      return False 
    if direction != None and new_direction != direction:
      return False

    return True

def check_report(report): 
  start = report[0]
  direction = None
  good_report = True
  for value in report[1:]:
    diff = value - start
    new_direction = abs(diff) == diff
    if not is_good_value(value, start, direction):
      good_report = False
      break
    direction = new_direction 
    start = value
  return good_report


good_reports = 0
for report in data:
  if check_report(report):
    good_reports += 1

print(good_reports)


# --------------------- Part 2 --------------------- #

data = parse_puzzle_input()
data = parse_puzzle_input(True)

def check_report_2(report): 
  start = report[0]
  direction = None
  for index in range(1, len(report)):
    value = report[index]
    diff = value - start
    new_direction = abs(diff) == diff
    if not is_good_value(value, start, direction):
      report_a = report[0:index-2] + report[index-1:]
      report_b = report[0:index-1] + report[index:]
      report_c = report[0:index] + report[index+1:]
      report_d = report[0:index+1] + report[index+2:]
      all_reports = [report_a, report_b, report_c, report_d]

      if (any([check_report(r) for r in all_reports])):
        return True
      return False
      
    direction = new_direction 
    start = value
  return True


good_reports = 0
for report in data:
  if check_report_2(report):
    good_reports += 1

print(good_reports)


