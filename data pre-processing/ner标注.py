import jieba
import re
import codecs
import fileinput

f1 = open('C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例\\病例分词.txt', 'r', encoding='UTF-8-sig')
f2 = open("C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例标注\\tag1.txt","r",encoding="UTF-8-sig")
fout=open("C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例标注\\tag2.txt","w",encoding="UTF-8-sig")
lines1 = f1.readlines()
lines2 = f2.readlines()
for line1 in lines1:
    line1 = line1.strip().split()
    for i in line1:
        for line2 in lines2:
            line2 = line2.strip().split()
            for j in line2:
                if i==j:
                    i+='/'+line2[1]
        fout.write(''.join(i)+' ')
    fout.write('\n')

#word_list.insert(i, '/' + line[1])
#sentence = sentence.replace(line[0], line[1])
