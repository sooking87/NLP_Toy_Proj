import csv
import os
import pandas as pd

temp_df = pd.read_csv('charts.csv', index_col=False)
temp_df.drop_duplicates(subset='song', inplace=True)
temp_df.reset_index()
testTemp_df = temp_df.head(20)
# print(testTemp_df.keys())

# print(list(testTemp_df.keys()))

testTemp_df.to_csv("testData.csv", index=False)
