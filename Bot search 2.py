import tweepy
import botometer
import pandas as pd

rapidapi_key = "XXXXXXXXXXXXX"
twitter_app_auth = {
    'consumer_key': 'XXXXXXX',
    'consumer_secret': 'XXXXXXH',
    'access_token': 'XXXXXXXXXX',
    'access_token_secret': 'XXXXXXXX',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
column_names=['Original tweet id','id of the replies','created at','number of RT','number of fav','source','user','Number of followers','user account created at','user location','user description','user friends','user status','user verified?','text']
df = pd.read_csv("C:/Users/kevin/Downloads/block3/block3/projekte/python/pythonProject2/Replies to factchecking Websites - Copy/Boomlive_In_Replies/Boomlivein_replies31.csv", names=column_names)

print(df)
accounts=df.user.to_list()
users2=[]
results = bom.check_account(accounts)
for user in accounts:
    users2.append(results)
    print(users2)


#result = bom.check_account(1548959833)

# Check a sequence of accounts
#accounts = ['@clayadavis', '@onurvarol', '@jabawack']
#for screen_name, result in bom.check_accounts_in(accounts):
    # Do stuff with `screen_name` and `result`

#print(result)