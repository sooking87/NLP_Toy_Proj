import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./lyrics_sentiment_dataset/lyrics_sentiment_dataset_3.csv')

# df.shape : (2394, 8)
# filtered_df.shape : (2265, 8)
# 점수 중에 하나라도 0점이 있는 데이터: 129개
# filtered_df.count() : Null Zero
# filtered_df에서의 lyrics 평균길이: 6099

# drop_df = len_df.drop(len_df.index[0:30], inplace=False)
# filtered_df에서 내림차순 정렬 기준 앞에서부터 30개를 버리면 lyrics 평균길이 : 2508
# filtered_df에서 내림차순 정렬 기준 앞에서부터 50개를 버리면 lyrics 평균길이 : 1908

# 하나라도 0점이면 out
filtered_df = df[(df['neg_sentiment'] != 0.000) & (df['neu_sentiment'] != 0.000) & (df['pos_sentiment'] != 0.000) & (df['com_sentiment'] != 0.000)]

# lyrics 길이만 조작
get_len = []
for i in filtered_df.index.tolist():
    length = len(filtered_df.loc[i, 'lyrics'])
    filtered_df.loc[i, 'lyrics_len'] = length

# 
filtered_df.sort_values('lyrics_len', ascending=False, inplace=True)
print(filtered_df.head(30))

