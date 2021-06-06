#!/usr/bin/python3
import sys

#Reading in the data from the yelp file given as a Terminal command
#skipping the first line, to not include data headers
lines = sys.stdin.readlines()[1:]

#Splitting the data by commas (,)
for line in lines:
    words = line.split(",")
    
    #printing the business id, date checked in and the # of check ins for that specfic day
    #key equals to business id and date checked in, value will be the # of check ins that day
    print("%s, %s #%d" %(words[0], words[1], int(words[3])))
   