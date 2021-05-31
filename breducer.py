#!/usr/local/bin/python3


import sys, re


previous = None
sum = 0

input = open("bigrams.txt", 'w')
for line in sys.stdin:
    key,value =  line.split( '\t' )

    if key != previous:
        if previous is not None:
           input.write ( str( sum ) + '\t' + str(previous) + '\n' )
        previous = key
        sum = 0
   
    sum = sum + int(value)

input.write( str(sum) + '\t' + str(previous) + '\n')
input.close()