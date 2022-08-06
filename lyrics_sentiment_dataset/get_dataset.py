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
filtered_df = df[(df['neg_sentiment'] != 0.000) & (df['neu_sentiment'] != 0.000) & (
    df['pos_sentiment'] != 0.000) & (df['com_sentiment'] != 0.000)]

# lyrics 길이만 조작
get_len = []
for i in filtered_df.index.tolist():
    length = len(filtered_df.loc[i, 'lyrics'])
    filtered_df.loc[i, 'lyrics_len'] = length

# 우선 가사 길이가 긴 경우를 뽑고, 해당 가사가 맞는지 아닌지 확인
filtered_df.sort_values('lyrics_len', ascending=False, inplace=True)
print(filtered_df.head(30))

#
# lyrics_len 내림차순 정렬
filtered_df.sort_values('lyrics_len', ascending=False, inplace=True)

# 어디까지는 "무조건" 지워야하는지 확인 -> filtered_df 기준 인덱스 90까지 지워야됨
delete = filtered_df.iloc[0:91, 0:]
print(delete)
# 해당 가수의 가사 찾기
li = filtered_df[(filtered_df['artist_name'] == 'the brian jonestown massacre') & (
    filtered_df['track_name'] == 'fucker')]['lyrics'].tolist()
print(li)

fin_filtered_df = filtered_df.iloc[91:, 0:]

# 제일 마지막은 들어본 결과 가사가 없음 => del
short_lyrics = fin_filtered_df[(fin_filtered_df['artist_name'] == 'blues traveler') & (
    fin_filtered_df['track_name'] == 'the good, the bad and the ugly')].index

fin_filtered_df = fin_filtered_df.drop(short_lyrics)
fin_filtered_df.to_csv("lyrics_sentiment_dataset_3.csv")
