import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = 'Tc0FYXZcxlLrowDDUPOJ1q1xc'
consumer_secret = 'LMCrP3tVjjyNe1n8TdImp1f8kZrVqpeJCcXBW0a6M4JHobMckO'

access_token = '396203971-NRqLdHJqxml7gRsBT2ATZ5YcbXS1rvWJYkOnADG1'
access_token_secret = 'JMgRFUW5A7JZPmuKHLHfutDIofEe0fFx5XZH2wgs1Qkbv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 3 - Retrieve Tweets
public_tweets = api.search('tesla')

# CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
# and label each one as either 'positive' or 'negative', depending on the sentiment
# You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)

    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")