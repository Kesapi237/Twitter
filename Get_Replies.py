import csv
import tweepy
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Oauth keys
consumer_key = "XXXXXXXX"
consumer_secret = "XXXXXXX"
access_token = "XXXXXXX"
access_token_secret = "XXXXXXXXX"

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'politifact'
tweet_id = '1471946301009014784'


replies=[]
for tweet in tweepy.Cursor(api.search_tweets,q='to:'+name, result_type='recent', timeout=999999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)

with open('1471946301009014784.csv', 'w',encoding="utf-8") as f:
    csv_writer = csv.DictWriter(f, fieldnames=('id','created at','number of RT','number of fav','source','user','Number of followers','user account created at','user location','user description','user friends','user status','user verified?','text'))
    csv_writer.writeheader()
    for tweet in replies:
        row = {'id':tweet.id,'created at':tweet.created_at,'number of RT':tweet.retweet_count,'number of fav':tweet.favorite_count,'source':tweet.source, 'user': tweet.user.screen_name,'Number of followers': tweet.user.followers_count,'user account created at': tweet.user.created_at,'user location': tweet.user.location, 'user description':tweet.user.description,'user friends':tweet.user.friends_count,'user status':tweet.user.statuses_count,'user verified?':tweet.user.verified,'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)