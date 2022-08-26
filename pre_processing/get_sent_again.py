import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from nltk.stem import WordNetLemmatizer
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


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


print(df_prev['lyrics'][0])
print(get_lyric_sentiment(df_prev['lyrics'][0]))

for i in df_prev.index.tolist():
    print("\n%d번 째 인덱스" % i)
    sentiment = get_lyric_sentiment(df_prev['lyrics'][i])
    df_prev.loc[i, 'neg_sentiment'] = sentiment['neg']
    df_prev.loc[i, 'neu_sentiment'] = sentiment['neu']
    df_prev.loc[i, 'pos_sentiment'] = sentiment['pos']
    df_prev.loc[i,
                'com_sentiment'] = sentiment['compound']

df_prev.to_csv(
    "get_sent_agian_billboard_dataset.csv", index=False)
