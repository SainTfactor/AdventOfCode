#!/usr/bin/env python3
import argparse

def parse_puzzle_input(real_data=False):
  data_source = "real_data.txt" if real_data else "sample_data.txt"
  with open(data_source, "r") as f:
    data = [i.strip() for i in f.readlines()]

  rules = [[int(j) for j in i.split("|")] for i in data if "|" in i]
  jobs = [[int(j) for j in i.split(",")] for i in data if "," in i]

  return rules,jobs


def check_rule(job, rule):
  if rule[0] in job and rule[1] in job:
    if job.index(rule[0]) < job.index(rule[1]):
      return True
    else:
      return False
  else:
    return True


def fix_job(job, rule):
  loc_1 = job.index(rule[0])
  loc_2 = job.index(rule[1])
  job[loc_1] = rule[1]
  job[loc_2] = rule[0]

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="AoC Solver", description="This is a scaffold of an Advent of Code solver program.")
  parser.add_argument("-r", "--real", action="store_true", help="Use real data instead of sample data.")
  args = parser.parse_args()

  rules, jobs = parse_puzzle_input(args.real)

  # --------------------- Part 1 --------------------- #
 
  bad_jobs = []

  summary = 0
  for job in jobs:
    is_legit = True
    for rule in rules:
      if not check_rule(job, rule):
        is_legit = False
        break
    if is_legit:
      summary += job[int(len(job)/2)]
    else:
      bad_jobs.append(job)
  print(summary)

  # --------------------- Part 2 --------------------- #

  for job in bad_jobs:
    done=False
    while not done:
      done=True
      for rule in rules:
        if not check_rule(job,rule):
          done=False
          fix_job(job,rule)
          break

  print(sum([i[int(len(i)/2)] for i in bad_jobs]))






