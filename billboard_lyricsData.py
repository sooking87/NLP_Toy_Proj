import lyricsgenius
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Function to return song lyrics


def get_lyrics(title, artist):
    try:
        return genius.search_song(title, artist).lyrics
    except:
        return 'not found'

# Function to return sentiment score of each song


def get_lyric_sentiment(lyrics):
    sentiment = sid_obj.polarity_scores(lyrics)
    return sentiment


genius = lyricsgenius.Genius(
    "DuO42xKa4Ts70InLe_Y_strEpeL_CxowzCtXyAMaiNlbAOVOTfFpt2q5FdP4lo_U")
sid_obj = SentimentIntensityAnalyzer()

# sample: testData.csv / actual: charts.csv
billboard100_df = pd.read_csv('testData.csv')
billboard100_df = billboard100_df.drop(
    ['rank', 'last-week', 'peak-rank', 'weeks-on-board'], axis=1)
billboard100_df.drop_duplicates(subset='song', inplace=True)
billboard100_df.reset_index(drop=True)

# 노래 가사 불러오기
lyrics = billboard100_df.apply(lambda row: get_lyrics(
    row['song'], row['artist']), axis=1)
billboard100_df['lyrics'] = lyrics
print(billboard100_df.shape)
# not found 제거
billboard100_df = billboard100_df.drop(
    billboard100_df[billboard100_df['lyrics'] == 'not found'].index)
# print("after del not found: ", billboard100_df.shape)
# print(billboard100_df.index.tolist())

# Use get_lyric_sentiment to get sentiment score for all the song lyrics
sentiment = billboard100_df.apply(
    lambda row: get_lyric_sentiment(row['lyrics']), axis=1)

# print(sentiment)
# print(sentiment.index)
# print(type(sentiment))  # Series
# print(sentiment.values[0])  # -> sentiment score, type=dict

for i in billboard100_df.index.tolist():
    print("\n%d번 째 인덱스" % i)
    billboard100_df.loc[i, 'neg_sentiment'] = sentiment[i]['neg']
    billboard100_df.loc[i, 'neu_sentiment'] = sentiment[i]['neu']
    billboard100_df.loc[i, 'pos_sentiment'] = sentiment[i]['pos']
    billboard100_df.loc[i, 'com_sentiment'] = sentiment[i]['compound']

billboard100_df.to_csv("commit12.csv", index=False)
# df.read_csv(filename, index_col=False)
