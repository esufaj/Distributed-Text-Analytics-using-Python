#!/usr/bin/python
import sys, re

#previous is used to check the keys
previous = None
#sum is used to add the # of occurences of the current word
sum = 0

#Reading in the data from the umapper.py output given in terminal
for line in sys.stdin:
    #creating a key and value pair by using \t as a seperator
    #whereas key is the word and value corresponds to the initial value of 1
    key,value =  line.split( '\t' )

    #checks if the key word has been seen for the first time
    #prints to the terminal 
    if key != previous: 
        if previous is not None:
           print( str( sum ) + '\t' + previous + '\n' )
        previous = key #setting previous to key to mark it as seen, therefore if seen again add the value to its current value
        sum = 0
    #adding the # of occurences of each word
    sum = sum + int(value)

#printing the # of occurences corresponding to each key
print( str(sum) + '\t' + previous + '\n')
