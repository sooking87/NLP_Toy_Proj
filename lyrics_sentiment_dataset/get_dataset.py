import pandas as pd

df = pd.read_csv('./lyrics_sentiment_dataset/lyrics_sentiment_dataset_3.csv')
print(df.shape)
print(df.keys())
print(df['neg_sentiment'].value_counts().tolist(), '\n')
print(df['neu_sentiment'].value_counts().tolist(), '\n')
print(df['pos_sentiment'].value_counts().tolist(), '\n')
print(df['com_sentiment'].value_counts().tolist(), '\n') 