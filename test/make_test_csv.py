import csv
import os
import pandas as pd

temp_df = pd.read_csv('./charts.csv', index_col=False)
temp_df.drop_duplicates(subset='song', inplace=True)
temp_df.reset_index()
testTemp1_df = temp_df.iloc[0:10, 0:]
testTemp2_df = temp_df.iloc[10:20, 0:]

testTemp1_df.to_csv("billboard_sample1.csv", index=False)
testTemp2_df.to_csv("billboard_sample2.csv", index=False)
