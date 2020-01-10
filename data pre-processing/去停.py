# coding=utf-8
import jieba

input_path = "C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例\\result.txt"
output_path = "C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例\\result1.txt"
stopwords_path = "C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例\\stopwords.txt"

# 设置停用词
print('start read stopwords data.')
stopwords = []
with open(stopwords_path, 'r', encoding='utf-8') as f:
    for line in f:
        if len(line) > 0:
            stopwords.append(line.strip())


def tokenizer(s):
    words = []
    #cut = jieba.cut(s)
    for word in s:
        if word not in stopwords:
            words.append(word)
    return words

# 读取文件数据，分词，并输出到文件
with open(output_path, 'w', encoding='utf-8') as o:
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            s = tokenizer(line.strip())
            o.write("".join(s) + "\n")
