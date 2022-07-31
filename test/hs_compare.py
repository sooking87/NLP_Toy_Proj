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

# Function to return sentiment score of each song


def get_lyric_sentiment(lyrics):
    sentiment = sid_obj.polarity_scores(lyrics)
    return sentiment


genius = lyricsgenius.Genius(
    "DuO42xKa4Ts70InLe_Y_strEpeL_CxowzCtXyAMaiNlbAOVOTfFpt2q5FdP4lo_U")
sid_obj = SentimentIntensityAnalyzer()

hs_df = pd.read_csv('billboard_data.csv')
hs_df_head = hs_df.head(20)
print(hs_df_head)

# 노래 가사 불러오기
lyrics = hs_df_head.apply(lambda row: get_lyrics(
    row['title'], row['artist']), axis=1)
hs_df_head['Lyrics'] = lyrics
print(hs_df_head.shape)
# not found 제거
hs_df_head = hs_df_head.drop(hs_df_head[hs_df_head['Lyrics'] == 'not found'].index)

# Use get_lyric_sentiment to get sentiment score for all the song lyrics
sentiment = hs_df_head.apply(
    lambda row: get_lyric_sentiment(row['Lyrics']), axis=1)

for i in hs_df_head.index.tolist():
    print("\n%d번 째 인덱스" % i)
    hs_df_head.loc[i, 'neg_sentiment'] = sentiment[i]['neg']
    hs_df_head.loc[i, 'neu_sentiment'] = sentiment[i]['neu']
    hs_df_head.loc[i, 'pos_sentiment'] = sentiment[i]['pos']
    hs_df_head.loc[i, 'com_sentiment'] = sentiment[i]['compound']

hs_df_head.to_csv("sent_compare_2.csv")