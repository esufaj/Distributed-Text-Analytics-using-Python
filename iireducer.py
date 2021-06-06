#!/usr/bin/python3

import sys

#previous is used to check the keys
previous = None
#list of business ids
busIDS = []

#Reading in the data from the iimapper.py output given in terminal
for line in sys.stdin:
    #creating a key and value pair by using \t as a seperator
    #whereas key is the category and value corresponds to the business that has that tag as an identifier 
    key,value =  line.split( '\t' )
    value = value.strip('\n') #removes whitespace after business id

    #checks if the key has been seen for the first time
    #prints to the terminal 
    if key != previous:
        if previous is not None:
            #printing tag and all business ids associated with that tag
            print(previous + " " + ", ".join(busIDS) + "\n\n")

            busIDS.clear() #empty current business list
            busIDS.append(value) #add ids for next category
        #setting previous to key to mark it as seen, therefore if seen again add the value to the business list
        previous = key
    #accumlating a list of business ids when tag has been seen for that specific business
    if (key == previous and value not in busIDS):
        busIDS.append(value)
