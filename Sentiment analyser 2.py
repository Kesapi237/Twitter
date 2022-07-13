import pandas as pd
import re
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
import seaborn as sns
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Import some Tweets
df = pd.read_csv("C:/Users/kevin/PycharmProjects/pythonProject/Data from student/Data from student/Replies Tweets/20.02.22(Total)/Replies to factchecking Websites - Copy/APFactCheck_Replies/APTOTAL.csv")
df['text'] = df['text'].astype(str).str.lower()
tweets = df['text']

def remove_links(text):
    '''Takes a string and removes web links from it'''
    text = re.sub(r'http\S+', '', text) # remove http links
    text = re.sub(r'bit.ly/\S+', '', text) # rempve bitly links
    text = text.strip('[link]') # remove [links]
    return text

tweets=tweets.apply(remove_links)
def remove_users(text):
    '''Takes a string and removes retweet and @user information'''
    text = re.sub('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', text) # remove retweet
    text = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', text) # remove tweeted at
    return text
tweets=tweets.apply(remove_users)

my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@'
def clean_tweet(text):
    text = text.lower() # lower case
    text = re.sub('['+my_punctuation + ']+', ' ', text) # strip punctuation
    text = re.sub('\s+', ' ', text) #remove double spacing
    text = re.sub('([0-9]+)', '', text) # remove numbers
    return text
tweets=tweets.apply(clean_tweet)

regexp = RegexpTokenizer('\w+')
tweets=df['text'].apply(regexp.tokenize)
nltk.download('stopwords')
from nltk.corpus import stopwords

# Make a list of english stopwords
stopwords = nltk.corpus.stopwords.words('english')

# Extend the list with your own custom stopwords
my_stopwords = ['https','Politifact']
stopwords.extend(my_stopwords)

# Remove stopwords
tweets = tweets.apply(lambda x: [item for item in x if item not in stopwords])

# Remove words which occur less than 2 times
tweets = tweets.apply(lambda x: ' '.join([item for item in x if len(item)>2]))
nltk.download('wordnet')
wordnet_lem = WordNetLemmatizer()

tweets = tweets.apply(wordnet_lem.lemmatize)
all_words = ' '.join([word for word in tweets])
words = nltk.word_tokenize(all_words)
#fd = FreqDist(words)
# Obtain top 10 words
#top_10 = fd.most_common(10)
# Create pandas series to make plotting easier
#fdist = pd.Series(dict(top_10))
#sns.set_theme(style="ticks")

#sns.barplot(y=fdist.values, x=fdist.values, color='red');
#fig = px.bar(y=fdist.index, x=fdist.values)

# sort values
#fig.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})

# show plot
#fig.show()




nltk.download('vader_lexicon')


analyzer = SentimentIntensityAnalyzer()
df['polarity'] = tweets.apply(lambda x: analyzer.polarity_scores(x))
# Change data structure
df = pd.concat([df.drop(['Original tweet id','id of the replies','created at','number of RT',
                                               'number of fav','source','user','Number of followers',
                                               'user account created at','user location','user description',
                                               'user friends','user status','user verified?'], axis=1),df['polarity'].apply(pd.Series)],axis=1)

# Create new variable with sentiment "neutral," "positive" and "negative"
df['sentiment'] = df['compound'].apply(lambda x: 'positive' if x >0 else 'neutral' if x==0 else 'negative')
# Tweet with highest positive sentiment

#print(df.loc[df['compound'].idxmax()].values)
# Tweet with highest negative sentiment
# ...seems to be a case of wrong classification because of the word "deficit"
#print(df.loc[df['compound'].idxmin()].values)

sns.countplot(y='sentiment',
             data=df,
             palette=['#b2d8d8',"#008080", '#db3d13']
             );
plt.show()