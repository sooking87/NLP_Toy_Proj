import pandas as pd

df_prev = pd.read_csv(
    "./pre_processing/lyrics_sentiment_dataset_3_tokenized.csv")
df_again = pd.read_csv(
    "./pre_processing/get_sent_again_lyrics_sentiment_dataset_3_tokenized.csv")

print(df_prev.head())
print(df_again.head())
