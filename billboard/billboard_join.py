import pandas as pd

temp1_df = pd.read_csv('billboard_sample1.csv', index_col=False)
temp2_df = pd.read_csv('billboard_sample2.csv', index_col=False)
final_df = pd.concat([temp1_df, temp2_df], ignore_index=True)
final_df.reset_index()

print(final_df)
final_df.to_csv("billboard_sample_total.csv", index=False)
