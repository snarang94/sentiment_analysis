import csv
import filesname

# Creating an empty list
tweetList = []
indexList = []
cleanedFile = 'final.csv'
positiveList = []
negativeList = []
positive = 0
negative = 0
sentiment_value = ''

# Opening cleaned tweet CSV to read tweets
with open(filesname.cleandata) as myTweetsCsv:
    tweetCsvReader = csv.DictReader(myTweetsCsv)
    for record in tweetCsvReader:
        tweetList.append(record['Tweets'])


# This functions finds all the indexes of a specified word from the CSV
def findIndexes(csv, word):
    indices = -1
    while True:
        indices = csv.find(word, indices + 1)
        if indices == -1:
            break
        yield indices


# Opening Sentiword dictionary
with open('SentiWords.txt', 'r') as dictionary:
    sentiWordDictionary = dictionary.read()

''' Get positive and negative sentiment values function
    flag 1: positive
    flag 0(or any other): negative 
'''


def get_positive_negative(ind, point_end, point_start, flag):
    while (not sentiWordDictionary[point_end].isalpha() or sentiWordDictionary[point_end] in '\n'):
        point_end = point_end + 1
    if (flag == 1):
        temp = sentiWordDictionary[point_start: point_end].replace('\n', '')
        temp = temp.replace('#', '')
        temp = temp.replace('_', '')
        temp = temp.replace('-', '')
        if len(temp) > 1:
            if float(temp[0]) == 0 and float(temp[1].isdigit()):
                temp = 0.1
        if float(temp) > 1:
            temp = 0.1
        positiveList.append(temp)
    else:
        temp = sentiWordDictionary[point_start: point_end].replace('\n', '')
        temp = temp.rstrip('-')
        negativeList.append(temp)


# Sentiment CSV file headings
sentiment_headings = ['tweet', 'sentiment_value', 'sentiment']
with open('sentiment.csv', 'w') as writeSentiment:
    sentimenttWriter = csv.writer(writeSentiment, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
    sentimenttWriter.writerow(sentiment_headings)

i = 1
for tweets in tweetList:
    print("processing..." + str(i))
    words = tweets.split(' ')
    for word in words:
        indexList.append(list(findIndexes(sentiWordDictionary, word.lower())))
        if (not len(indexList) == 0):
            for index in indexList:
                for ind in index:
                    if (sentiWordDictionary[ind - 1] in '\n' and sentiWordDictionary[ind + len(word)] in '#'):
                        point_start = ind + len(word) + 3
                        point_end = point_start

                        if (sentiWordDictionary[point_end].isdigit() or sentiWordDictionary[point_end] in '.'):
                            # Positive sentiment function call
                            get_positive_negative(ind, point_end, point_start, 1)
                            break
                        if (sentiWordDictionary[point_end] in '-'):
                            # Negative sentiment function call
                            get_positive_negative(ind, point_end, point_start, 0)
                            break
                            # Summing positive any negatove sentiments
    for values in positiveList:
        positive = positive + float(values)
    for values in negativeList:
        negative = negative + float(values)

    # Calculating sentiment value
    sentiment_value = (positive + negative) / len(words)

    # Classifying sentiment as neutral, positive or negative
    if sentiment_value == 0:
        sentiment = 'neutral'
    elif sentiment_value >= 0:
        sentiment = 'positive'
    else:
        sentiment = 'negative'
    positiveList = []
    negativeList = []

    # Writing the sentiments to CSV file
    csvList = [tweets, sentiment_value, sentiment]
    with open(filesname.sentimentalfinal, 'a') as mySentimentFile:
        wr = csv.writer(mySentimentFile, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        wr.writerow(csvList)
    i = i + 1
