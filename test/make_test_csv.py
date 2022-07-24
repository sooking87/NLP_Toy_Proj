import csv
import os
import pandas as pd

temp_df = pd.read_csv('Hot Stuff.csv')
temp_df.drop_duplicates(subset='SongID', inplace=True)
temp_df.reset_index()
testTemp_df = temp_df.tail(20)
# print(testTemp_df.keys())
testTemp_df = testTemp_df.drop(['WeekID', 'Week Position', 'SongID', 'Instance', 'Previous Week Position', 'Peak Position',
                                'Weeks on Chart'], axis=1)
# print(list(testTemp_df.keys()))

testTemp_df.to_csv("testData.csv", index=False)
