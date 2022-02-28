import nltk
nltk.download('averaged_perceptron_tagger')


from textblob import TextBlob

text = '''
your opinion is bias'''

blob = TextBlob(text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

for sentence in blob.sentences:
    a=sentence.sentiment.polarity
    print(a)
    if a > 0:
        print("positive")
    elif a == 0:
        print("neutral")
    else:
        print("negative")
