# script to scrape tweets using a search keyword

import GetOldTweets3 as got
import csv
import pandas as pd
from textblob import TextBlob

max_tweets = 200

tweetCriteria = got.manager.TweetCriteria().setQuerySearch("environment")\
                                           .setMaxTweets(max_tweets)\
                                           .setNear("39.50, 98.35")\
                                           .setWithin("900mi")\
                                           .setSince("2017-01-20")\
                                           .setUntil("2019-11-21")\
                                           .setLang("en")

num_tweets = 0
polarity = 0


df = pd.DataFrame(columns=['tweet','military','healthcare','immigration','environment','gun control', 'economy','taxes',
                           'education','foreign policy','polarity'])

for i in range(1,max_tweets):
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]

    analysis = TextBlob(tweet.text)  # analyzes the string

    if (analysis.polarity) != 0 and ("http" not in tweet.text) and (".com" not in tweet.text):

        df = df.append({'tweet': tweet.text , 'polarity' : analysis.polarity}, ignore_index=True)

        num_tweets = num_tweets + 1
        print(tweet.text)


print(num_tweets)


df.to_csv("/Users/tanushrees/Documents/environment_tweets.csv", index=False)
