#!/usr/bin/env python3
import requests
import argparse

session_id="53616c7465645f5f6c99a02fcc8d6aa806234692c2cf31a5d8d2ac04dffbcfd693e1db11f5c35d46f7eb6838a15f63f7"

def get_input(day):
    global session_id
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
