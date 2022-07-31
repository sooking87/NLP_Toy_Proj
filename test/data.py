import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import lyricsgenius

# Function to return song lyrics


def get_lyrics(title, artist):
    try:
        return genius.search_song(title, artist).lyrics
    except:
        return 'not found'


def get_lyric_sentiment(lyrics):
    sentiment = sid_obj.polarity_scores(lyrics)
    return sentiment


genius = lyricsgenius.Genius(
    "DuO42xKa4Ts70InLe_Y_strEpeL_CxowzCtXyAMaiNlbAOVOTfFpt2q5FdP4lo_U")
sid_obj = SentimentIntensityAnalyzer()

df = pd.read_csv('tcc_ceds_music.csv')
sample_df = df.tail(10)
sample_df.drop_duplicates(subset="track_name", inplace=True)
sample_df.reset_index()
print(sample_df)

# 노래 가사 불러오기
lyrics = sample_df.apply(lambda row: get_lyrics(
    row['track_name'], row['artist_name']), axis=1)
sample_df['Lyrics'] = lyrics
print(sample_df.shape)
# not found 제거
sample_df = sample_df.drop(sample_df[sample_df['Lyrics'] == 'not found'].index)
# print("after del not found: ", sample_df.shape)
print(sample_df.index.tolist())

# Use get_lyric_sentiment to get sentiment score for all the song lyrics
sentiment = sample_df.apply(
    lambda row: get_lyric_sentiment(row['Lyrics']), axis=1)
print(sentiment)
print(sentiment.keys())
for i in sample_df.index.tolist():
    print("\n%d번 째 인덱스" % i)
    sample_df.loc[i, 'neg_sentiment'] = sentiment[i]['neg']
    sample_df.loc[i, 'neu_sentiment'] = sentiment[i]['neu']
    sample_df.loc[i, 'pos_sentiment'] = sentiment[i]['pos']
    sample_df.loc[i, 'com_sentiment'] = sentiment[i]['compound']

sample_df.to_csv("sample_df_2.csv")
