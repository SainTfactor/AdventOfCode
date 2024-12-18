#!/usr/bin/env python3
import os
import requests
import argparse
from datetime import datetime

def get_input(day, year):
    session_id = ""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, "session_id.dat")
    with open(filepath, "r") as f:
        session_id=f.read().strip()
    s = requests.Session()
    s.cookies.set("session", session_id, domain="adventofcode.com")
    data = s.get("https://adventofcode.com/{}/day/{}/input".format(year,day))
    return data.text

def array_of_strings(data):
    return '["{}"]'.format('", "'.join([i for i in data.split("\n") if i != ""]))

def choose_display_type(data):
    if True:
        output = array_of_strings(data)
        print("data = {}".format(output))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Advent of Code input')
    parser.add_argument('-d', '--day', type=int, help='The day of the challenge you want your input for.')
    parser.add_argument('-y', '--year', type=int, help='The day of the challenge you want your input for.')
    args = parser.parse_args()

    year = args.year
    if year == None:
      year = datetime.now().year

    data = get_input(args.day, year)

    #print("#!/usr/bin/env python3")
    #choose_display_type(data)
    print(data, end="")
