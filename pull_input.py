#!/usr/bin/env python3
import requests
import argparse

def get_input(day):
    session_id = ""
    with open("session_id.dat", "r") as f:
        session_id=f.read().strip()
    s = requests.Session()
    s.cookies.set("session", session_id, domain="adventofcode.com")
    data = s.get("https://adventofcode.com/2021/day/{}/input".format(day))
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
    args = parser.parse_args()

    data = get_input(args.day)

    print("#!/usr/bin/env python3")
    choose_display_type(data)
