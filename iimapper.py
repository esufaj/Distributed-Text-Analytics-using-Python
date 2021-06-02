#!/usr/local/bin/python3

import sys

# input = open("tester_2.txt", 'w')

lines = sys.stdin.readlines()[1:]

for line in lines:  
    busIDS = line.split(",")
    tagList = busIDS[len(busIDS)-1].split(';')

    for  category in tagList:
        # if '\r\n' in category:
        category = category.rstrip('\r\n')
        
        print(category + "\t" + busIDS[0])
        # input.write(category + "\t" + busIDS[0] + "\n")

# input.close()