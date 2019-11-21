# script to scrape tweets using a search keyword

import GetOldTweets3 as got
from textblob import TextBlob

tweetCriteria = got.manager.TweetCriteria().setQuerySearch("military")\
                                           .setMaxTweets(100)\
                                           .setNear("39.50, 98.35")\
                                           .setWithin("900mi")\
                                           .setSince("2017-01-20")\
                                           .setUntil("2019-11-20")

num_tweets = 0
polarity = 0

for i in range(1,10):

    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]

    analysis = TextBlob(tweet.text)  # analyzes the string

    if (analysis.polarity) != 0:
        polarity = polarity + analysis.polarity
        num_tweets = num_tweets + 1
        print(tweet.text)  # .text turns it into a strings
        print(analysis.polarity)
        print("\n")


print("average polarity is")
print (polarity/num_tweets)
print(num_tweets)