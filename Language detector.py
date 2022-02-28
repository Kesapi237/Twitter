from langdetect import detect_langs
import pandas as pd
column_names=['Original tweet id','id of the replies','created at','number of RT','number of fav','source','user','Number of followers','user account created at','user location','user description','user friends','user status','user verified?','text']
df = pd.read_csv("C:/Users/kevin/Downloads/block3/block3/projekte/python/pythonProject2/Replies to factchecking Websites - Copy/Snopes_Replies/Snopes_replies31.csv", names=column_names)
myText=df.text.to_list()

languages = []

for text in myText:
    languages.append((text, detect_langs(text)))
    print(languages)
#df = pd.read_csv("C:/Users/kevin/Downloads/block3/block3/projekte/python/pythonProject2/Replies to factchecking Websites - Copy/LeadStoriesCom_Replies/LeadstoriesCom_replies31.csv", names=column_names)
#df["Languages"] = languages
#df.to_csv("C:/Users/kevin/Downloads/block3/block3/projekte/python/pythonProject2/Replies to factchecking Websites - Copy/LeadStoriesCom_Replies/LeadstoriesCom_replies31.csv", index=False)
#print(detect_langs(text))
