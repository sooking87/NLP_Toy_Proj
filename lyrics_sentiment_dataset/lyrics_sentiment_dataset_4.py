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
lyrics_sentiment_dataset = pd.read_csv('./lyrics_sentiment_dataset/tcc_ceds_music.csv', encoding='cp949')
print(lyrics_sentiment_dataset.keys())
lyrics_sentiment_dataset = lyrics_sentiment_dataset.drop(
    ['Unnamed: 0', 'genre',
       'lyrics', 'len', 'dating', 'violence', 'world/life', 'night/time',
       'shake the audience', 'family/gospel', 'romantic', 'communication',
       'obscene', 'music', 'movement/places', 'light/visual perceptions',
       'family/spiritual', 'like/girls', 'sadness', 'feelings', 'danceability',
       'loudness', 'acousticness', 'instrumentalness', 'valence', 'energy',
       'topic', 'age'], axis=1)

lyrics_sentiment_dataset.drop_duplicates(subset='track_name', inplace=True)
lyrics_sentiment_dataset.reset_index(drop=True)  
lyrics_sentiment_dataset_4 = lyrics_sentiment_dataset.iloc[14191:18920, 0:]

# 노래 가사 불러오기
lyics1 = lyrics_sentiment_dataset_4.apply(lambda row: get_lyrics(
    row['track_name'], row['artist_name']), axis=1)
lyrics_sentiment_dataset_4['lyrics'] = lyics1
print(lyrics_sentiment_dataset_4.shape)
# not found 제거
lyrics_sentiment_dataset_4 = lyrics_sentiment_dataset_4.drop(
    lyrics_sentiment_dataset_4[lyrics_sentiment_dataset_4['lyrics'] == 'not found'].index)
# print("after del not found: ", lyrics_sentiment_dataset_4.shape)
# print(lyrics_sentiment_dataset_4.index.tolist())

# Use get_lyric_sentiment to get sentiment score for all the song lyrics
sentiment = lyrics_sentiment_dataset_4.apply(
    lambda row: get_lyric_sentiment(row['lyrics']), axis=1)

# print(sentiment)
# print(sentiment.index)
# print(type(sentiment))  # Series
# print(sentiment.values[0])  # -> sentiment score, type=dict

for i in lyrics_sentiment_dataset_4.index.tolist():
    # print("\n%d번 째 인덱스" % i)
    lyrics_sentiment_dataset_4.loc[i, 'neg_sentiment'] = sentiment[i]['neg']
    lyrics_sentiment_dataset_4.loc[i, 'neu_sentiment'] = sentiment[i]['neu']
    lyrics_sentiment_dataset_4.loc[i, 'pos_sentiment'] = sentiment[i]['pos']
    lyrics_sentiment_dataset_4.loc[i, 'com_sentiment'] = sentiment[i]['compound']

lyrics_sentiment_dataset_4.to_csv("lyrics_sentiment_dataset_4.csv", index=False)