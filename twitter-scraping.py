# script to scrape tweets using a search keyword

import GetOldTweets3 as got
import pandas as pd
from textblob import TextBlob

max_tweets = 200

# change QuerySearch parameter based on feature
tweetCriteria = got.manager.TweetCriteria().setQuerySearch("foreign policy")\
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

# for each tweet
for i in range(1,max_tweets):
    num_tweets = num_tweets+1
    print(num_tweets)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]

    # analyze string
    analysis = TextBlob(tweet.text)

    # if polarity is not 0 and tweet does not contain a link to an image
    if (analysis.polarity) != 0 and ("http" not in tweet.text) and (".com" not in tweet.text):

        #append the tweet and polarity to the dataframe
        df = df.append({'tweet': tweet.text , 'polarity' : analysis.polarity}, ignore_index=True)


df.to_csv("/Users/tanushrees/Documents/foreign_policy_tweets.csv", index=False)