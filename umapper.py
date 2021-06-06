#!/usr/bin/python
import sys,re

#Reading in the data from the yelp file given as a Terminal command
for line in sys.stdin:

    #Splitting the first column in the data set (the text column)
    #Removing characters that are not part of the word column such as
    #special characters and white space
    line = line.split(",")[0]
    line = re.sub(r'^\W+|\W+$','',line)
    words = re.split(r"\W+",line)
    words = list(filter(None, words))
    
    #Iterating through the list of words and printing the word with an
    #initial value of 1
    for word in words:
        print(word.lower() + "\t1")