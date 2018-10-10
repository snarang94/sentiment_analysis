#### Sentimental Analysis
The purpose of this application is to Extract, Transform and Load tweets while performing Sentimental Analysis on it.  We have to perform Sentiment Analysis on a thousand tweets and fetch score of each tweet. For that we Twitter developer API to fetch tweets from the Twitter based on specific keywords

##### Prerequisites

Install Python
Install PyCharm

###### Libraries 
- re
- string
- csv
- tweepy
- elasticsearch

##### Executing the code

1. Execute the **FetchingTweets.py** file to fetch the tweets and export them to dirtydata.csv
2. Once executed, clean the tweets by executing **CleaningTweets.py** which will give cleandata.csv.
3. The above csv created will be used for Sentimental Analysis. For this run **Sentimental.py** which will generate sentimental.csv, having polarity and sentiments.
4. Finally run **ElasticSearch.py** to transfer the data to the index db in cloud.

#####References

[1] Gatti, Lorenzo, Marco Guerini, and Marco Turchi. "SentiWords: Deriving a high precision and high coverage lexicon for sentiment analysis." IEEE Transactions on Affective Computing 7.4 (2016): 409-421.

[2] Guerini M., Gatti L. & Turchi M. “Sentiment Analysis: How to Derive Prior Polarities from SentiWordNet”. In Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing (EMNLP'13), pp 1259-1269. Seattle, Washington, USA. 2013.+

[3] Warriner A. B., Kuperman V. & Brysbaert M. "Norms of valence, arousal, and dominance for 13,915 English lemmas". Behavior research methods, 45(4), 1191-1207. 2013.

[4] “13.1. csv - CSV File Reading and Writing,” 16.2. Threading - Higher-level threading interface - Python 2.7.15 documentation. [Online]. Available: https://docs.python.org/2/library/csv.html. [Accessed: 07-Oct-2018]

[5] “Helpers,” Python Elasticsearch Client - Elasticsearch 6.3.0 documentation. [Online]. Available: https://elasticsearch-py.readthedocs.io/en/master/helpers.html. [Accessed: 09-Oct-2018].

[6] “re - Regular expression operations,” 16.2. Threading - Higher-level threading interface - Python 2.7.15 documentation. [Online]. Available: https://docs.python.org/3/library/re.html. [Accessed: 09-Oct-2018].
