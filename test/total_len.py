import pandas as pd

df = pd.read_csv('./charts.csv', index_col=False)
df.drop_duplicates(subset='song', inplace=True)
df.reset_index()
print(df.shape)
