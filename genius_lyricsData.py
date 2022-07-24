# install modules
"""
pip install lyricsgenius
pip install vaderSentiment
pip install pandas
"""
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

# temp: testData.csv, actual: Hot Stuff.csv
hot100_df = pd.read_csv('Hot Stuff.csv')
# 노래 중복 제거
hot100_df.drop_duplicates(subset='SongID', inplace=True)  # actual: SongID로 바꾸기
hot100_df.reset_index(drop=True)
print(hot100_df.shape)

# 노래 가사 불러오기
lyrics = hot100_df.apply(lambda row: get_lyrics(
    row['Song'], row['Performer']), axis=1)
hot100_df['Lyrics'] = lyrics
print(hot100_df.shape)
# not found 제거
hot100_df = hot100_df.drop(hot100_df[hot100_df['Lyrics'] == 'not found'].index)
# print("after del not found: ", hot100_df.shape)
print(hot100_df.index.tolist())

# Use get_lyric_sentiment to get sentiment score for all the song lyrics
sentiment = hot100_df.apply(
    lambda row: get_lyric_sentiment(row['Lyrics']), axis=1)

print(sentiment)
print(sentiment.index)
print(type(sentiment))  # Series
# print(sentiment.values[0])  # -> sentiment score, type=dict

for i in hot100_df.index.tolist():
    print("\n%d번 째 인덱스" % i)
    hot100_df.loc[i, 'neg_sentiment'] = sentiment[i]['neg']
    hot100_df.loc[i, 'neu_sentiment'] = sentiment[i]['neu']
    hot100_df.loc[i, 'pos_sentiment'] = sentiment[i]['pos']
    hot100_df.loc[i, 'com_sentiment'] = sentiment[i]['compound']

hot100_df.to_csv("commit12.csv")
