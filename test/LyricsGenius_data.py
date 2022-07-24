# import lyricsgenius
# genius = lyricsgenius.Genius(
#     "DuO42xKa4Ts70InLe_Y_strEpeL_CxowzCtXyAMaiNlbAOVOTfFpt2q5FdP4lo_U")

# artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
# song = artist.song("To You")
# print(song.lyrics)
# artist.save_lyrics()

# install modules
# pip install lyricsgenius
# pip install textblob
# python -m textblob.download_corpora
# pip3 install gensim==3.6.0
# Function to return lyrics of each song using Genius API

from textblob import TextBlob
from gensim.summarization import keywords
import nltk
from nltk.corpus import stopwords
from spacy.lang.en import English
import spacy
import lyricsgenius
import pandas as pd


def get_lyrics(title, artist):
    try:
        return genius.search_song(title, artist).lyrics
    except:
        return 'not found'


# Function to return sentiment score of each song
def get_lyric_sentiment(lyrics):
    analysis = TextBlob(lyrics)
    return analysis.sentiment.polarity

# Function to preprocess text


def preprocess(text):
    # Create Doc object
    doc = nlp(text, disable=['ner', 'parser'])
    # Generate lemmas
    lemmas = [token.lemma_ for token in doc]
    # Remove stopwords and non-alphabetic characters
    a_lemmas = [lemma for lemma in lemmas
                if lemma.isalpha() and lemma not in stopwords]

    return ' '.join(a_lemmas)


"""Extract Keywords from text"""


def return_keywords(texts):
    xkeywords = []
    values = keywords(text=preprocess(texts), split='\n', scores=True)
    for x in values[:10]:
        xkeywords.append(x[0])
    try:
        return xkeywords
    except:
        return "no content"


# import packages
nltk.download('stopwords')
stopwords = set(stopwords.words('english'))
nlp = English()
nlp.max_length = 10000000

genius = lyricsgenius.Genius(
    "DuO42xKa4Ts70InLe_Y_strEpeL_CxowzCtXyAMaiNlbAOVOTfFpt2q5FdP4lo_U")


# import billboard hot100 dataset
hot100_df = pd.read_csv('Hot Stuff.csv')
# remove duplicate occurrences of songs
hot100_df.drop_duplicates(subset='SongID', inplace=True)
hot100_df.reset_index(drop=True)


# Use get_lyrics funcion to get lyrics for every song in dataset
lyrics = hot100_df.apply(lambda row: get_lyrics(
    row['Song'], row['Performer']), axis=1)
hot100_df['Lyrics'] = lyrics
# drop rows where lyrics are not found on Genius
hot100_df = hot100_df.drop(hot100_df[hot100_df['Lyrics'] == 'not found'].index)

# Use get_lyric_sentiment to get sentiment score for all the song lyrics
sentiment = hot100_df.apply(
    lambda row: get_lyric_sentiment(row['Lyrics']), axis=1)
hot100_df['Sentiment'] = sentiment

# Resample daraframe lyrics by year. Get all the lyrics for every song for each year
lyrics_resample = hot100_df['Lyrics'].resample('Y').sum()

# Use return_keywords function on lyrics_resample to get the top 20 keywords for each year
lyric_keywords = [return_keywords(x[1]) for x in lyrics_resample.iteritems()]
