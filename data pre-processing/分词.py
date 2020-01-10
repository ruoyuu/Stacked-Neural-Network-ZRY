# -*- coding=utf8 -*-
import jieba
import re

jieba.load_userdict("dic.txt")

fp=open('F:\\数据\\train_data600\\病例result.txt', 'r', encoding='UTF-8-sig')
fout=open('F:\\数据\\train_data600\\分词.txt', 'w', encoding='UTF-8-sig')
for line in fp.readlines():
    words=jieba.cut(line)
    result=" ".join(words)
    fout.write(result)
