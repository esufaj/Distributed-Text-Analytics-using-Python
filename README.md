# **Distributed Text Analytics Using Python**

#### In this project, I have designed and implemented a number of MapReduce algorithms for performing distributed analytics on textual data.The dataset is a subset of Yelp's which was originally put together for the Yelp Dataset Challenge and contains seven CSV files including information about businesses across 11 metropolitan areas in four countries and can be accessed here (registration to Kaggle is required):Yelp dataset:https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6Yelp. The first set of the MapReduce algorithms compute n-grams of business tips; the second set computes popularity of a business; the third set computes an inverted index of the business categories. These are important statistics and tools commonly used in computational linguistic and information retrieval tasks. ####

---------------------------------------------------------------------------------------------------------------
#### **A. Distributed Computation of n-grams**
  In the fields of computational linguistics, an n-gram is a contiguous sequence of n-items from a given sample of text. For this part of the project, I assume that  items are words collected from yelp business reviews. An n-gram of size 1 is referred to as a “unigram”; of size 2 is a “bigram”; of size 3 is a “trigram”. For example, given the text input “I love ice cream” the following unigrams, bigrams and trigrams are computed: unigrams→(“I”, “love”, “ice”, “cream”) bigrams→(“I love”, “love ice”, “ice cream”) trigrams→(“I love ice”, “love ice cream”). I have created a MapReduce algorithm that when given a collection of business reviews as input, I get as ouput:
  
  1) The number of occurrences of each unigram in the review collection (umapper.py, ureducer.py).
  2) Compute the number of occurrences of each bigram in the review collection (bmapper.py, breducer.py).
  3) Compute the number of occurrences of each trigram in the tips collection (tmapper.py, treducer.py).

  The data will be written to their respective files and tested through Docker using the HDFS environment.

---------------------------------------------------------------------------------------------------------------
#### **B. Distributed Computation of business popularity by day of the week** 
  In this part of the project, I have created a MapReduce algorithm that when given a collection of yelp checkins as input, I get as output:
  
  1) Compute the aggregated number of checkins per day of the week for each business (checkinsmapper.py and checkinsreducer.py). The output will be in the form of: 
     Business1, Mon, Business1 checkins
     Business1, Tue, Business1 checkins
     ...
     ...
     Business2, Mon, Business2 checkins
     ...
     
  The data will be written to their respective files and tested through Docker using the HDFS environment.

---------------------------------------------------------------------------------------------------------------
#### **C. Distributed Construction of an Inverted Index** 
  In information retrieval, an inverted index is an index data structure that stores a mapping from words to a collection of documents that they appear in. A further explanation is that I have built a MapReduce algorithm that computes an inverted index that maps categories (of businesses) to businesses. In other words, given a collection of businesses (as provided by Yelp), an inverted index is a dictionary where each category is associated with a list of the business ids that belong to that category. Thus, when given a dataset of businesses as input, I get as output:
  
  1) An inverted index of the categories to businesses (iimaper.py, iireducer.py).

  The data will be written to a file in the format of a table where column1 has a business and column2 has a comma seperate list of categories associated with that business. This has been tested through Docker using the HDFS environment.

---------------------------------------------------------------------------------------------------------------
#### **HOW TO RUN:** 

#### Conventional way: 

PART A: for unigrams, bigrams and trigrams: python3 *mapper.py < yelp_tip.csv | sort | *reducer.py
PART B: python3 checkinsmapper.py < yelp_checkins.csv | sort | checkinsreducer.py
PART C: python3 iimapper.py < yelp_business.csv | sort | iireducer.py

-----------------------------------------------------------------------------------------------------------
#### Using docker & Hadoop to run MapReduce:

step 1: (for easy adding into docker image folder) cd into your working directory

step 2: (running a docker image, creating a folder called app and adding the working directory to the created folder) docker run -it -v $PWD:/app eecsyorku/eecs4415

step 3: (creating a folder in Hadoop) hdfs dfs -ls /

step 4: (for adding files into Hadoop to run) hdfs dfs -put ./*mapper.py /.  *DO THIS FOR ANY FILES TRYING TO BE RUN IN HADOOP AS WELL AS INPUT FILES SUCH AS *reducer.py or inputs such as yelp_tip.csv etc...*

step 5: (for running MapReduce algos in Hadoop) hadoop jar /usr/hadoop-3.0.0/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -mapper /app/*mapper.py  -reducer /app/*reducer.py -input /yelp_*.csv -output /output

step 6: (for getting output) hdfs dfs -get /output/part* .

IF YOU NEED TO REMOVE OUTPUT USE: rm part-0000
