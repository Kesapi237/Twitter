import text2emotion as te
import pandas as pd
import re
import nltk
column_names=['Original tweet id','id of the replies','created at','number of RT','number of fav','source','user','Number of followers','user account created at','user location','user description','user friends','user status','user verified?','text']
df = pd.read_csv("C:/Users/kevin/Downloads/block3/block3/projekte/python/pythonProject2/Replies 20.02.22/Replies to factchecking Websites - Copy/LeadStoriesCom_Replies/LeadStoriestotal.csv", names=column_names)

myText=df.text.to_list()
emotion = []

for text in myText:
    emotion.append((text, te.get_emotion(text)))
    print(emotion)
#result=te.get_emotion(myText)

#print(result)
