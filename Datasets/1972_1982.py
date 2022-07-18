import csv
import os

os.chdir(r"C:\STUDY\방학(3)\NLP_Toy_Proj")

header = [['year', 'artist', 'title', 'lyrics', 'sentiment'],
          [1, 2, 3, 4, 5]]


def writecsv(filename, the_list):
    with open(filename, 'w', newline='') as f:
        a = csv.writer(f, delimiter=',')
        a.writerows(the_list)


def opencsv(filename):
    f = open(filename, 'r', encoding='utf-8')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output
    f.close()


#writecsv("abc.csv", header)
# output = opencsv("abc.csv")
# print(output)
