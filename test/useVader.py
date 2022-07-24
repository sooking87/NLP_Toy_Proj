from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import lyricsgenius

genius = lyricsgenius.Genius(
    "DuO42xKa4Ts70InLe_Y_strEpeL_CxowzCtXyAMaiNlbAOVOTfFpt2q5FdP4lo_U")
sid_obj = SentimentIntensityAnalyzer()

lyrics = genius.search_song("Dynamite", "BTS").lyrics
sentiment = sid_obj.polarity_scores(lyrics)
print("%s, %s, sentiment:" % ("BTS", "Dynamite"), end=' ')
print(sentiment)

lyrics2 = genius.search_song("Fall For You", "Secondhand Serenade").lyrics
sentiment2 = sid_obj.polarity_scores(lyrics2)
print("%s, %s, sentiment:" %
      ("Secondhand Serenade", "Fall For You"), end=' ')
print(sentiment2)

print(sentiment.keys())
