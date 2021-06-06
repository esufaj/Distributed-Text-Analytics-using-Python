#!/usr/bin/python3

import sys

#previous is used to check the keys
previous = None
#sum is used to add the # of occurences of the current word triplet
sum = 0

#Reading in the data from the tmapper.py output given in terminal
for line in sys.stdin:
    #creating a key and value triplet pair by using \t as a seperator
    #whereas key is the word triplet and value corresponds to the initial value of 1
    key,value =  line.split( '\t' )

    #checks if the key word triplet has been seen for the first time
    #prints to the terminal 
    if key != previous:
        if previous is not None:
           print( str( sum ) + '\t' + str(previous) + '\n' )
        previous = key #setting previous to key to mark it as seen, therefore if seen again add the value to its current value
        sum = 0
    #adding the # of occurences of each word triplet
    sum = sum + int(value)
#printing the # of occurences corresponding to each word triplet
print( str(sum) + '\t' + str(previous) + '\n')
