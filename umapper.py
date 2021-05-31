#!/usr/local/bin/python3
import sys,re
# import nltk
# from nltk.tokenize import RegexpTokenizer
# from nltk import word_tokenize 
# from nltk.util import ngrams


# input = open("tester.txt", 'w')
# inputFile = sys.stdin


for line in sys.stdin:
    # line = line.replace('"', "")
#     line = re.sub('"', '', line)
    
#     line = line.replace("'","").replace('"', '')
    line = line.split(",")[0]
    line = re.sub(r'^\W+|\W+$','',line)
    words = re.split(r"\W+",line)
#     words = words.strip().split()
    # token = word_tokenize(words)
#     txtSet = []
#     txtSet.append(words[0])

#     tokenizer = RegexpTokenizer("[\w']+")
#     words = tokenizer.tokenize(txtSet[0])
    # token = word_tokenize(txtSet[0])
    



#     unigram = ngrams(words, 1)
    # print(unigram)


    for word in words:
#         # token = word_tokenize(words)
        
        # input.write( word.lower() + "\t1" + "\n")

        print(word.lower() + "\t1")
# input.close()

        # r'(\w+\'\w+|^[A-Za-z]*$)'
        # [^A-Za-z0-9 ]+
        # [\w']+






# import sys
# import re



# for line  in sys.stdin:
#     line = line.split(",", 1)[0]
#     words = line.strip().split()

#     for word in words:
#         print(word.lower() + "\t1")