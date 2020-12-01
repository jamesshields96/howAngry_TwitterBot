import tweepy as tw
import pandas as pd
import os
import datetime


CONSUMER_KEY = "CONSUMER_KEY"
CONSUMER_SECRET = "CONSUMER_SECRET"
ACCESS_KEY = "ACCESS_KEY"
ACCESS_SECRET = "ACCESS_SECRET"


def connect_to_twitter_OAuth():
    auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tw.API(auth)
    return api


# Create API object
api = connect_to_twitter_OAuth()


search = "#" + \
    input("What hashtag would you like to search for? ") + " -filter:retweets"
date = datetime.datetime.now()
year = int(date.strftime("%Y"))
month = int(date.strftime("%m"))
day = int(date.strftime("%d"))
pos = 0
neg = 0

if month == 1:
    date_since = str(year - 1) + "-" + "12" + "-" + str(day)
else:
    date_since = str(year) + "-" + str(month - 1) + "-" + str(day)

tweets = tw.Cursor(api.search, q=search, lang="en", since=date_since).items(20)
user_data = []

for tweet in tweets:
    print(tweet.text)
    print("---------")
    search_word = tweet.text.split()
    user_data.append([tweet.user.screen_name, tweet.user.location])

    if any(x in search_word for x in ('good', 'great', 'awesome', 'happy', 'excellent', 'fantastic', 'fun', 'excited')):
        pos += 1
    elif any(x in search_word for x in ('bad', 'terrible', 'broken', 'unsub', 'stupid', 'dumb', 'horrible', 'annoying')):
        neg += 1


print("Positive tweets: " + str(pos) + " Negative tweets: " + str(neg))






tweet_info = pd.DataFrame(data=user_data, columns=['user', "location"])

tweet_info.to_csv(
    r'C:\Users\James\Documents\School\Projects\howAngry_TwitterBot\tweet_info.csv', index=False, header=True)


print(tweet_info)