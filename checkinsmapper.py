#!/usr/local/bin/python3
import sys,re
# import nltk
# from nltk.tokenize import RegexpTokenizer
# from nltk import word_tokenize 
# from nltk.util import ngrams


# input = open("tester10.txt", 'w')
# inputFile = sys.stdin

lines = sys.stdin.readlines()[1:]

for line in lines:
    # line = line.replace('"', "")
    # line = re.sub('"', '', line)
    
    # line = line.replace("'","").replace('"', '')


#------------ Method 1 ---------------- (both methods give same unpacking error, need to fix)

    words = line.split(",")
    # businessID = words[0]
    # dayCheck = words[1]
    # values = words[3]
    # words.remove(words[2])
    # businessID.strip('\n')
    # dayCheck.strip('\n')
    # values.strip('\n')
    print("%s, %s#%d" %(words[0], words[1], int(words[3])))    
    # print(words)
    # input.write(str(words) + "\n")
    # token = word_tokenize(words)
    # txtSet = []
    # txtSet.append(words[0])

    # tokenizer = RegexpTokenizer("[\w']+")
    # words = tokenizer.tokenize(txtSet[0])
    # token = word_tokenize(txtSet[0])
    



    # triple = list(ngrams(words, 3))
    # input.write(str(unigram) + "\n")


    # for word in triple:

        # token = word_tokenize(words)
        
    # input.write( str(words[0]) + ", " + str(words[1]) + ", #" + str(words[2]) + "\n")
        # print(words[0] + ", " + words[1] + ", #" + words[2])
        # print(word[0] + ", " + word[1] + ", # 1")
# input.close()

        # r'(\w+\'\w+|^[A-Za-z]*$)'
        # [^A-Za-z0-9 ]+
        # [\w']+






#----------- Method 2 -----------------

# inputFile = sys.stdin

# lines = sys.stdin.readlines()[1:]

# for line in lines:
#     words = line.split(",")
#     words.remove(words[2])

#     triple = list(ngrams(words, 3))

#     for word in triple:
#         print(word[0] + ", " + word[1] + ", #" + word[2])
        #input.write( str(words[0]) + ", " + str(words[1]) + ", #" + str(words[2]) + "\n")

# input.close()