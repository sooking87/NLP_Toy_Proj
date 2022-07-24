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

"""sample: billboard_sample1.csv / actual: charts.csv"""
billboard100_1_df = pd.read_csv('billboard_sample1.csv')
billboard100_1_df = billboard100_1_df.drop(
    ['rank', 'last-week', 'peak-rank', 'weeks-on-board'], axis=1)
billboard100_1_df.drop_duplicates(subset='song', inplace=True)
billboard100_1_df.reset_index(drop=True)

# 노래 가사 불러오기
lyics1 = billboard100_1_df.apply(lambda row: get_lyrics(
    row['song'], row['artist']), axis=1)
billboard100_1_df['lyrics'] = lyics1
print(billboard100_1_df.shape)
# not found 제거
billboard100_1_df = billboard100_1_df.drop(
    billboard100_1_df[billboard100_1_df['lyrics'] == 'not found'].index)
# print("after del not found: ", billboard100_1_df.shape)
# print(billboard100_1_df.index.tolist())

# Use get_lyric_sentiment to get sentiment score for all the song lyrics
sentiment1 = billboard100_1_df.apply(
    lambda row: get_lyric_sentiment(row['lyrics']), axis=1)

# print(sentiment1)
# print(sentiment1.index)
# print(type(sentiment1))  # Series
# print(sentiment1.values[0])  # -> sentiment1 score, type=dict

for i in billboard100_1_df.index.tolist():
    print("\n%d번 째 인덱스" % i)
    billboard100_1_df.loc[i, 'neg_sentiment'] = sentiment1[i]['neg']
    billboard100_1_df.loc[i, 'neu_sentiment'] = sentiment1[i]['neu']
    billboard100_1_df.loc[i, 'pos_sentiment'] = sentiment1[i]['pos']
    billboard100_1_df.loc[i, 'com_sentiment'] = sentiment1[i]['compound']

billboard100_1_df.to_csv("billboard_dataset.csv", index=False)

"""sample: billboard_sample2.csv / actual: charts.csv"""
billboard100_2_df = pd.read_csv('billboard_sample2.csv')
billboard100_2_df = billboard100_2_df.drop(
    ['rank', 'last-week', 'peak-rank', 'weeks-on-board'], axis=1)
billboard100_2_df.drop_duplicates(subset='song', inplace=True)
billboard100_2_df.reset_index(drop=True)

# 노래 가사 불러오기
lyrics2 = billboard100_2_df.apply(lambda row: get_lyrics(
    row['song'], row['artist']), axis=1)
billboard100_2_df['lyrics'] = lyrics2
print(billboard100_2_df.shape)
# not found 제거
billboard100_2_df = billboard100_2_df.drop(
    billboard100_2_df[billboard100_2_df['lyrics'] == 'not found'].index)
# print("after del not found: ", billboard100_2_df.shape)
# print(billboard100_2_df.index.tolist())

# Use get_lyric_sentiment to get sentiment score for all the song lyrics
sentiment2 = billboard100_2_df.apply(
    lambda row: get_lyric_sentiment(row['lyrics']), axis=1)

# print(sentiment2)
# print(sentiment2.index)
# print(type(sentiment2))  # Series
# print(sentiment2.values[0])  # -> sentiment2 score, type=dict

for i in billboard100_2_df.index.tolist():
    print("\n%d번 째 인덱스" % i)
    billboard100_2_df.loc[i, 'neg_sentiment'] = sentiment2[i]['neg']
    billboard100_2_df.loc[i, 'neu_sentiment'] = sentiment2[i]['neu']
    billboard100_2_df.loc[i, 'pos_sentiment'] = sentiment2[i]['pos']
    billboard100_2_df.loc[i, 'com_sentiment'] = sentiment2[i]['compound']

billboard100_2_df.to_csv("billboard_sample2.csv", index=False)
