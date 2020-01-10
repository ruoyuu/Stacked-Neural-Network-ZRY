# coding=utf-8
import jieba

input_path = "F:\\数据\\train_data600\\RES.txt"
output_path = "F:\\数据\\train_data600\\pos.txt"
#stopwords_path = "C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例\\stopwords2.txt"


#stopwords = []
#with open(stopwords_path, 'r', encoding='utf-8') as f:
    #for line in f:
        #if len(line) > 0:
            #stopwords.append(line.strip())
#def tokenizer(s):
    #words = []
    #for word in s:
        #if word not in stopwords:
            #words.append(word)
    #return words

# 读取文件数据，分词，并输出到文件
with open(output_path, 'w', encoding='utf-8') as o:
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            #a = tokenizer(line.strip())
            #b=("".join(a))
            s = line.replace('解剖部位','body')
            s1 = s.replace('药物','cure')
            s2 = s1.replace('症状描述','symp')
            s3 = s2.replace('独立症状', 'dise')
            s4 = s3.replace('手术', 'chec')
            #s5 = s4.replace('\t\t\t','\t')
            o.write(s4+'\n')


