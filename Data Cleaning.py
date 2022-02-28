import pandas as pd
import re
import nltk
column_names=['Original tweet id','id of the replies','created at','number of RT','number of fav','source','user','Number of followers','user account created at','user location','user description','user friends','user status','user verified?','text']
df = pd.read_csv("C:/Users/kevin/Downloads/block3/block3/projekte/python/pythonProject2/Replies 20.02.22/Replies to factchecking Websites - Copy/LeadStoriesCom_Replies/LeadStoriestotal.csv", names=column_names)
df.drop(columns=['Original tweet id','id of the replies','created at','number of RT',
                                               'number of fav','source','user','Number of followers',
                                               'user account created at','user location','user description',
                                               'user friends','user status','user verified?'], axis=1).sample(56)
myText=df.text.to_list()
emotion = []
def remove_links(text):
    '''Takes a string and removes web links from it'''
    text = re.sub(r'http\S+', '', text) # remove http links
    text = re.sub(r'bit.ly/\S+', '', text) # rempve bitly links
    text = text.strip('[link]') # remove [links]
    return text

def remove_users(text):
    '''Takes a string and removes retweet and @user information'''
    text = re.sub('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', text) # remove retweet
    text = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', text) # remove tweeted at
    return text

my_stopwords = nltk.corpus.stopwords.words('english')
word_rooter = nltk.stem.snowball.PorterStemmer(ignore_stopwords=False).stem
my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@'
def clean_tweet(text, bigrams=False):
    text = remove_users(text)
    text = remove_links(text)
    text = text.lower() # lower case
    text = re.sub('['+my_punctuation + ']+', ' ', text) # strip punctuation
    text = re.sub('\s+', ' ', text) #remove double spacing
    text = re.sub('([0-9]+)', '', text) # remove numbers
    text_token_list = [word for word in text.split(' ')
                            if word not in my_stopwords] # remove stopwords

    text_token_list = [word_rooter(word) if '#' not in word else word
                        for word in text_token_list] # apply word rooter
    if bigrams:
        text_token_list = text_token_list+[text_token_list[i]+'_'+text_token_list[i+1]
                                            for i in range(len(text_token_list)-1)]
    text = ' '.join(text_token_list)
    return text
df = df.text.apply(clean_tweet)

print(df)