#!/usr/bin/python3

import sys

#Reading in the data from the yelp file given as a Terminal command
#skipping the first line, to not include data headers
lines = sys.stdin.readlines()[1:]

#Splitting words by commas (,) to seperate indivdual columns
#Splitting the last column in the data set by semi-colon (;) to sperate individual tags 
for line in lines:  
    busIDS = line.split(",")
    tagList = busIDS[len(busIDS)-1].split(';')

    #iterating through tags, stripping away whitespace and unnecssary new lines
    for  category in tagList:
        # if '\r\n' in category:
        category = category.rstrip('\r\n')
        
        #printing tag (category) and the corresponding business ids that have that specific tag
        print(category + "\t" + busIDS[0])
