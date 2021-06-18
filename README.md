# a2
HOW TO RUN: 
Conventional way: 
PART A: for unigrams, bigrams and trigrams: python3 *mapper.py < yelp_tip.csv | sort | *reducer.py
PART B: python3 checkinsmapper.py < yelp_checkins.csv | sort | checkinsreducer.py
PART C: python3 iimapper.py < yelp_business.csv | sort | iireducer.py

EECS4415Big Data Systems Summer 2021Assignment 2(20%): Distributed Text Analytics using PythonDue Date: 11:59 pmon Friday, Jun 4, 2021ObjectiveIn  this assignment,  you  will  be designing  and  implementing  MapReduce  algorithms  for performing distributed analytics on textual data.The dataset is a subset of Yelp1's was originally put together for the Yelp  Dataset  Challengeand contains  seven  CSV  files  including information  about  businesses  across  11 metropolitan areas in four countriesand can be accessed here (registration to Kaggle is required):Yelp dataset:https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6Yelp dataset(local copy): https://www.eecs.yorku.ca/course_archive/2020-21/S/4415/yelp-data.zipThe first set of the MapReduce  algorithms compute n-grams ofbusiness tips; the  secondset computes popularity of a business; the third set computes an inverted index of the business categories. These are important statistics and tools commonly used in computational linguistic and information retrieval tasks.Important Notes:•You must use the submitcommand to electronically submit your solution by the due date. •Your programs should be tested on thedocker image that we provided before being submitted. •All programs are to be written using Python 3and to get full marks, code must be documented.What to SubmitWhen you have completed the assignment, move or copy your python scripts and outputs in a directory (e.g., assignment2), and use the following command to electronically submit your files:% submit4415 a2umapper.py ureducer.py unigrams.txt bmapper.py breducer.py bigrams.txt tmapper.py treducer.py trigrams.txt frequency-computation.txt checkinsmapper.py checkinsreducer.py checkinsbyday.txtiimaper.py iireducer.py inverted-index.txt team.txtThe team.txtfile  includes  information  about  the  team  members  (first  name,  last  name,  student  ID, login,  yorku  email). You  can  also  submit  the  files  individually  after  you  complete  each  part  of  the assignment–simply execute the submitcommand and give the filename that you wish to submit. Make sure you name your files exactlyas stated. You may check the status of your submission as following:% submit -l 4415a21Yelp. http://www.yelp.com

A. Distributed Computation of n-grams (35%, 5% each)In  the  fields  of  computational  linguistics,  an n-gramis  a  contiguous  sequence  of nitems  from  a  given sample of text. For this part of the assignment you can assume that items are wordscollected from yelp business  tips.An n-gram  of  size  1  is  referred  to  as  a “unigram”; of size  2  is  a “bigram”; of  size  3  is  a “trigram”.For example, given the text input“I love ice cream”the following unigrams, bigrams and trigrams are computed:unigrams→(“I”, “love”, “ice”, “cream”)bigrams→(“I love”, “love ice”, “ice cream”)trigrams→(“I love ice”, “love ice cream”)Your task is to design and implement MapReduce algorithms that given acollection of business tips:•compute the  number  of  occurrences  of  each unigramin the tips collection (umapper.py, ureducer.py)and output the results in a file called unigrams.txt•compute the  number  of  occurrences  of  each bigramin the tipscollection(bmapper.py, breducer.py)and output the results in a file called bigrams.txt•compute the  number  of  occurrences  of  each trigramin  the tipscollection  (tmapper.py, treducer.py)and output the results in a file called trigrams.txt•how would youmodify these scriptsin order to compute the frequencyof each of the quantities(instead of the number of occurrences)? Provide a short answer in plain text (up to half a page)with the name frequency-computation.txtThe collection of business tips is provided in a file yelp_tip.csvthat follows the same format as the original data set provided by Kaggle.The contents of the file mightvary when testing your code.Running the script:The following webpage  provides useful information on how  to test your scripts first locallyand then in the Hadoop environment:https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

B. Distributed Computation ofbusiness popularityby day of the week (25%)Design  and  implement  MapReduce  algorithms  that  given  a  collection  of yelp  checkins, compute the aggregated number of checkins per day of the week for each business. Your mapper and reducer should be named checkinsmapper.pyand checkinsreducer.py, respectivelythey should output the results in a file called checkinsbyday.txtThe output file checkinsbyday.txtlooks like:Yelp_business_1, Mon, #checkinsYelp_business_1, Tue, #checkins...Yelp_business_1, Sun, #checkinsYelp_business_2, Mon, #checkinsYelp_business_2, Tue, #checkins...Yelp_business_2, Sun, #checkins...The checkin information is provided in afile yelp_checkin.csvthat follows the same format as the original data set provided by Kaggle. The contents of the file mightvary when testing your code.Running the script:Similar to instructions provided in Part A.

C. Distributed Construction of an Inverted Index (40%)In information retrieval, an inverted index is an index data structure that  storesa mapping from wordstoa collection  of  documentsthat  they  appear  in. Your  task  is to  build  an inverted index  that  mapscategories (of businesses)to businesses. In other words, given a collection of businesses(as provided by Yelp), an inverted index  is a dictionary where each category is associated with a list of the business ids that belong to that category.See the example below:Your task is to design and implement MapReduce algorithms that given a collection of Yelp businesses:•compute the inverted index ofthe categories to businesses (iimaper.py, iireducer.py) and output the results in a file called inverted-index.txtThe collection of businesses is provided in a file yelp_business.csvthat follows the same format as the original data set provided by Kaggle. The contents of the file might vary when testing your code.Running the script:Similar to instructions provided in Part A.
