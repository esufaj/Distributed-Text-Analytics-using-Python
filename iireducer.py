#!/usr/local/bin/python3

import sys

previous = None
busIDS = []

# input = open("inverted-index.txt", 'w')

for line in sys.stdin:
    key,value =  line.split( '\t' )
    value = value.strip('\n')

    if key != previous:
        if previous is not None:
            print(previous + " " + ", ".join(busIDS) + "\n\n")

            busIDS.clear()
            busIDS.append(value)
        previous = key
    
    if (key == previous and value not in busIDS):
        busIDS.append(value)

# input.close()