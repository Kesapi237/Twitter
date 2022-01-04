import tweepy
import csv
import pandas as pd
# Here are my credentials from my twitter dev account
consumer_key = 'XXXXXXX'
consumer_secret= 'XXXXXX'
access_token='XXXXXX'
access_token_secret = 'XXXXXXXXX'

#Enter the name of the user
userID= "politifact"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
with open('Politifact_ID.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for status in api.user_timeline(screen_name=userID,count=3000):
        print(status.id)
        csvwriter.writerow([status.id])