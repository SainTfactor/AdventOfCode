#!/usr/bin/env python3
import fileinput
from pull_input import *

if __name__ == "__main__":
    data = "\n".join([line for line in fileinput.input()])
    choose_display_type(data)
