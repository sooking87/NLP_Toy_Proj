import pandas as pd

df_1 = pd.read_csv(
    './full_lyrics_dataset/lyrics_sentiment_dataset_1.csv', index_col=False)
df_2 = pd.read_csv(
    './full_lyrics_dataset/lyrics_sentiment_dataset_2.csv', encoding='utf-8', index_col=False)
df_3 = pd.read_csv(
    './full_lyrics_dataset/lyrics_sentiment_dataset_3.csv', index_col=False)
df_4 = pd.read_csv(
    './full_lyrics_dataset/lyrics_sentiment_dataset_4.csv', index_col=False)
df_5 = pd.read_csv(
    './full_lyrics_dataset/lyrics_sentiment_dataset_5.csv', index_col=False)
df_6 = pd.read_csv(
    './full_lyrics_dataset/lyrics_sentiment_dataset_6.csv', index_col=False)

final_df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6], ignore_index=True)
final_df.reset_index()

print(final_df)
# final_df.to_csv("full_lyrics_dataset.csv", index=False)
