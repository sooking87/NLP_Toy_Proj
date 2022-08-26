
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


def lemmatizer(tokenzied_list):
    lemmatized_list = []
    for word in tokenzied_list:
        word = lemma.lemmatize(word)
        lemmatized_list.append(word)
    return lemmatized_list


def get_lyric_sentiment(lyrics):
    sentiment = sid_obj.polarity_scores(lyrics)
    return sentiment


lemma = WordNetLemmatizer()
sid_obj = SentimentIntensityAnalyzer()


df_prev = pd.read_csv(
    "./pre_processing/billboard_dataset.csv")

model = Word2Vec(df_prev.loc[0:5, "lyrics"],
                 window=5, min_count=5)
print(model)
