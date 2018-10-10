import csv
import tweepy
import json
import filesname




# defining keys
consumer_key = "0SBMoUafUNgqD7ALagMOxDFG6"
consumer_secret = "TzClgvZ6fKzZjpSqOGUgPWBE3uag0T9ZgVVueBr5cAQa2BCLP4"
access_key = "1044557262012985346-ANNgnihJzy6MblsegRtaxpEkFIJv0H"
access_secret = "OOMOVeRVazzKImPyJLYpEf41rHsAEdNK2adNpuJWwpSny"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def get_tweets(query):
    try:
        tweets = api.search(query, count=1000)
    except tweepy.error.TweepError as e:
        tweets = [json.loads(e.response.text)]

    return tweets


queries = ["@BrockLesnar", "@WWERollins", "@God", "#Thor", "#Batman", "@Hulk", "@WWE", "#RAW",
           "@BellaTwins", "@WWERomanReigns", "#Engineer"]

i = 0
with open(filesname.dirtydata, 'w') as outfile:
    writer = csv.writer(outfile, lineterminator="\n")
    writer.writerow(['id', 'user', 'created_at ', 'text'])

    for query in queries:
        t = get_tweets(query)
        for tweet in t:
            i = i+1
            print("Writing...."+str(i)+" tweet")
            try:
                writer.writerow([tweet.id_str, tweet.user.screen_name, tweet.created_at, tweet.text.
                                encode('cp850', 'replace').decode('cp850')])
            except Exception:
                pass

    print("....ENDED....")

