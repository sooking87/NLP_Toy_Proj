import pandas as pd

df = pd.read_csv(
    './join_dataset/lyrics_sentiment_dataset_3.csv')

# df.columns = ['artist', 'title', 'year', 'lyrics', 'neg_sentiment',
#               'neu_sentiment', 'pos_sentiment', 'com_sentiment']

print(df.keys())
print(df.shape)
