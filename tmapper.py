#!/usr/bin/python3
import sys,re

#Reading in the data from the yelp file given as a Terminal command
for line in sys.stdin:
    
    #Splitting the first column in the data set (the text column)
    #Removing characters that are not part of the word column such as
    #special characters and white space
    line = line.split(",")[0]
    line = re.sub(r'^\W+|\W+$','',line)
    words = re.split(r"\W+",line)
    
    #iterating through triple pair of words and printing the words with an
    #initial value of 1
    for i in range(len(words) - 2):
        print(words[i].lower() +" "+ words[i + 1].lower() + " " + words[i + 2].lower() +  "\t1")
