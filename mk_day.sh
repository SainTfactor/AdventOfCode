#!/bin/bash

year=$1
day=$2

mkdir -p ./$year/$day
if [ ! -f ./$year/$day/sol.py ]; then
  cp scaffold.py ./$year/$day/sol.py
fi
touch ./$year/$day/real_data.txt
touch ./$year/$day/sample_data.txt
