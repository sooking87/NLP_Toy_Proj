import pandas as pd

df = pd.read_csv("lyrics_sentiment_dataset_5.csv")
df_prev = pd.read_csv("lyrics_sentiment_dataset_5_del_col.csv")
#print(df.iloc[:, 0:8])
print(df.index)
print(df.shape)
print(df.iloc[0:30, 0:])
print(df_prev.shape)
