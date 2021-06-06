#!/usr/bin/python3

import sys

#previous is used to check the keys
previous = None
#sum is used to add the # of check ins
sum = 0

#Reading in the data from the checkinsmapper.py output given in terminal
for line in sys.stdin:
    #creating a key and value pair by using # as a seperator
    #whereas key is the business id and date checked in and value corresponds to the # of check ins that day
    key,value =  line.split( '#' )
    
    #checks if the key pair has been seen for the first time
    #prints to the terminal 
    if key != previous:
        if previous is not None:
           print( previous + ', #' + str(sum) + '\n' )
        previous = key #setting previous to key to mark it as seen, therefore if seen again add the value to its current value
        sum = 0

    #adding the # of check ins per day
    sum = sum + int(value)
#printing the business id and date checked in also the total # of check ins for each corresponding day
print( previous + ', #' + str(sum) + '\n')
