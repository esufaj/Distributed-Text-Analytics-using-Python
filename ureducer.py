#!/usr/local/bin/python3

import sys, re


previous = None
sum = 0

input = open("unigrams.txt", 'w')
for line in sys.stdin:
    key,value =  line.split( '\t' )

    if key != previous:
        if previous is not None:
           input.write ( str( sum ) + '\t' + previous + '\n' )
        previous = key
        sum = 0
   
    sum = sum + int(value)

input.write( str(sum) + '\t' + previous + '\n')
input.close()