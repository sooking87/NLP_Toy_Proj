from textblob import TextBlob
import pandas as pd
import lyricsgenius
import spacy
from spacy.lang.en import English
from nltk.corpus import stopwords
import nltk
#from gensim.summarization import keywords

# import packages
nltk.download('stopwords')
stopwords = set(stopwords.words('english'))
nlp = English()
nlp.max_length = 10000000

genius = lyricsgenius.Genius(
    "DuO42xKa4Ts70InLe_Y_strEpeL_CxowzCtXyAMaiNlbAOVOTfFpt2q5FdP4lo_U")


def get_lyrics(title, artist):
    try:
        return genius.search_song(title, artist).lyrics
    except:
        return 'not found'


# song = genius.search_artist("BTS", max_songs=3, sort="title")
# print(song)

lyrics = genius.search_song("Dynamite", "BTS").lyrics
# print(lyrics)

analysis = TextBlob(lyrics)
sentiment = analysis.sentiment.polarity
print(sentiment)
