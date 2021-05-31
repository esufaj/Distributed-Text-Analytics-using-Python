#!/usr/bin/python

import sys, re


previous = None
sum = 0

input = open("checkinsbyday.txt", 'w')
for line in sys.stdin:
    key,value =  line.split( '#' )

    if key != previous:
        if previous is not None:
           input.write ( previous + ', #' + str(sum) + '\n' )
        previous = key
        sum = 0
   
    sum = sum + int(value)

input.write( previous + ', #' + str(sum) + '\n')
input.close()