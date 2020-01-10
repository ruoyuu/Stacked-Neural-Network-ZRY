#--*encoding=utf8-*-
import jieba
import jieba.posseg as pseg

################
fin=open('C:\\Users\\79844\\Desktop\\数据\\train_data600\\2\\病例1.txt','r',encoding='utf8')
fout=open('C:\\Users\\79844\\Desktop\\数据\\train_data600\\2\\病例2.txt','w',encoding='utf8')
for line in fin:
    if line:
        line=line.replace("\n","")
        line=line.strip()
        tag=pseg.cut("line")

        strTag=''
        for each in tag:
            if len(each)==2:
                temp= each[0]+"/"+each[1]+" "
                strTag+=temp
        fout.write(strTag+'\n')
fout.close()




