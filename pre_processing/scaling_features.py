import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn import preprocessing

df_prev = pd.read_csv(
    "./pre_processing/lyrics_sentiment_dataset_3_tokenized.csv")
df_again = pd.read_csv(
    "./pre_processing/get_sent_again_lyrics_sentiment_dataset_3_tokenized.csv")


y = df_prev['com_sentiment']
X = df_prev.drop(['neg_sentiment', 'neu_sentiment',
                 'pos_sentiment', 'com_sentiment'], axis=1)
print(X.keys)
