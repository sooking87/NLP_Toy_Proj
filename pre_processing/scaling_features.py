
import pandas as pd
import operator


def to_list(str):
    split_str = str.split(" ")
    return split_str

# 새로운 불용어와 기존 불용어 필터링하기


def filter_stopwords(tokenized_words, stopwords):
    tokenized_filtered = []

    for word in tokenized_words:
        if word not in stopwords:
            tokenized_filtered.append(word)

    return tokenized_filtered


def word_count(tokenized_data):
    word_counter = {}

    for i in tokenized_data:
        if i in word_counter.keys():
            word_counter[i] += 1
        else:
            word_counter[i] = 1

    # 많이 나온 순서대로 정렬

    sorted_dict = dict(sorted(word_counter.items(),
                              key=operator.itemgetter(1), reverse=True))

    return sorted_dict

# 가장 상위 20개의 단어 보기


def top_30(tokenized_dict):
    top_30_words = list(tokenized_dict.items())[:30]
    return top_30_words


df = pd.read_csv(
    "./pre_processing/renew_dataset_final.csv")

add_stopwords = ['ill', 'youll', 'well', 'till', 'shes', 'hes', 'shed', 'hed']
for i in range(10):
    # transform
    tokenized_list = to_list(df.loc[i, 'lyrics'])
    tokenized_filtered = filter_stopwords(tokenized_list, add_stopwords)
    count_dict = word_count(tokenized_filtered)
    top_30_list = top_30(count_dict)
    print(top_30_list)

    print("\n")
