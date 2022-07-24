from textblob import TextBlob
import pandas as pd
import lyricsgenius
import spacy
from spacy.lang.en import English
from nltk.corpus import stopwords
import nltk
# from gensim.summarization import keywords

genius = lyricsgenius.Genius(
    "DuO42xKa4Ts70InLe_Y_strEpeL_CxowzCtXyAMaiNlbAOVOTfFpt2q5FdP4lo_U")


# song = genius.search_artist("BTS", max_songs=3, sort="title")
# print(song)

lyrics = genius.search_song("Dynamite", "BTS").lyrics
# print(lyrics)

analysis = TextBlob(lyrics)
sentiment = analysis.sentiment.polarity
# print(type(sentiment))
print("%s, %s, sentiment: %.3f" % ("BTS", "Dynamite", sentiment))


lyrics2 = genius.search_song("Fall For You", "Secondhand Serenade").lyrics
# print(lyrics2)

analysis2 = TextBlob(lyrics2)
sentiment2 = analysis2.sentiment.polarity
print("%s, %s, sentiment: %.3f" %
      ("Secondhand Serenade", "Fall For You", sentiment2))
