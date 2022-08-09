import pandas as pd
from nltk import sent_tokenize
import nltk
nltk.download('punkt')

df = pd.read_csv('./lyrics_sentiment_dataset/lyrics_sentiment_dataset_3.csv')

text_sample = df.iloc[200, 0:]['lyrics']
print(text_sample)
sentences = sent_tokenize(text=text_sample)
print(sentences)
print(len(sentences))
