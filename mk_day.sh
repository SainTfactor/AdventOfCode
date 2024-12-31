#!/bin/bash

year=$1
day=$2

if [ "$day" == "" ]; then
  echo "Usage: ./mk_day.sh <year> <day>"
  exit
fi  

mkdir -p ./$year/$day
if [ ! -f ./$year/$day/sol.py ]; then
  cp scaffold.py ./$year/$day/sol.py
fi
if [ ! -f ./$year/$day/real_data.txt ]; then
  python3 pull_input.py -y $1 -d $2 > ./$year/$day/real_data.txt
fi
touch ./$year/$day/sample_data.txt
echo "pushd ./$year/$day/"
