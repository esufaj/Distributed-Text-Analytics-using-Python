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
    # line = re.sub('"', '', line)
    line = line.split(",")[0]
    line = re.sub(r'^\W+|\W+$','',line)
    words = re.split(r"\W+",line)
    # line = line.replace("'","").replace('"', '')

    # words = line.split(",")
    # token = word_tokenize(words)
    # txtSet = []
    # txtSet.append(words[0])

    # tokenizer = RegexpTokenizer("[\w']+")
    # words = tokenizer.tokenize(txtSet[0])
    # token = word_tokenize(txtSet[0])
    



    # unigram = list(ngrams(words, 2))
    # print(unigram)


    for i in range(len(words) - 1):
        # token = word_tokenize(words)
        
        # input.write( word[0].lower() + " "+ word[1].lower() + "\t1" + "\n")

        print(words[i] +" "+ words[i + 1] + "\t1")
# input.close()

        # r'(\w+\'\w+|^[A-Za-z]*$)'
        # [^A-Za-z0-9 ]+
        # [\w']+





#         ans = []
# text = ['cant railway station','citadel hotel',' police stn']
# for line in text:
#     arr = line.split()
#     for i in range(len(arr)-1):
#         ans.append([[arr[i]], [arr[i+1]]])