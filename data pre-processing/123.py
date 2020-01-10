import codecs
import sys

input_data = codecs.open("C:\\Users\\79844\\.anaconda\\demo\\BiGRU\\data\\ccks2018ES.txt","r",encoding="UTF-8-sig")
output_data = codecs.open("C:\\Users\\79844\\.anaconda\\demo\\BiGRU\\data\\ccks2018.txt","w",encoding="UTF-8-sig")
for line in input_data.readlines():
    word_list = line.strip().split()