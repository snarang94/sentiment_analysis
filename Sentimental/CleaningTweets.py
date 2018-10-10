import csv
import re
import string
import filesname

# empty list for copying only twitter column data
tweetIndex = []

# Copying tweets from csv to a list
with open(filesname.dirtydata) as myTweetsCsv:
    csvReader = csv.DictReader(myTweetsCsv)
    for tweet in csvReader:
        tweetIndex.append(tweet['text'])


# Remove punctuation and extra characters
def remove_punctuation(unfiltered_tweet):
    hyperlink_regexp = re.compile('(((https?)|(http?)):((\\\\)|(//))+([\d\w:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    single_tweets = re.findall(hyperlink_regexp, unfiltered_tweet)
    print("")
    for single_tweet in single_tweets:
        unfiltered_tweet = unfiltered_tweet.replace(single_tweet[0], '. ')


# Remove punctuation and extra characters

    unfiltered_tweet = unfiltered_tweet.replace('RT ', ' ')
    starting_symbols = ['#', '@']

    terms = []
    for punctuation in string.punctuation:
        if punctuation not in starting_symbols:
            print("")
            unfiltered_tweet = unfiltered_tweet.replace(punctuation, ' ')
    for term in unfiltered_tweet.split():
        term = term.strip()
        if term:
            print("")
            if term[0] not in starting_symbols:
                terms.append(term)

    final_term = ' '.join(terms)

    return final_term


# add filtered and clean tweet to the List
final_tweet = []


# calling clean functions
print("Removing Punctuations and Hyperlinks.......")
print("--------------------------------------------------------------------------------------------------------")

for tweet in tweetIndex:
    clean_tweet = remove_punctuation(tweet)
    final_tweet.append(clean_tweet)


# remove empty lines
try:
    final_tweet = list(filter(None, final_tweet))
except Exception:
    pass


# Header line for final cleaned csv
header = ['Tweets']

# handling rest of the dirty characters
[final_tweets.encode('utf-8') for final_tweets in final_tweet]


# uploading final cleaned tweets to csv

with open(filesname.cleandata, 'w') as final_csv:
        print("Writing cleaned tweets to csv.......")
        head = csv.writer(final_csv, lineterminator='\n')
        head.writerow(header)
        write = csv.writer(final_csv, quoting=csv.QUOTE_ALL,  delimiter='\n')
        write.writerow(final_tweet)

print("--------------------------------------------------------------------------------------------------------")
print("Job completed.....Check the file")
print("--------------------------------------------------------------------------------------------------------")




