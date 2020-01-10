
#coding:utf-8
import shutil
readDir = "C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例标注\\tag.txt"
writeDir = "C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例标注\\tag1.txt"
#txtDir = "/home/fuxueping/Desktop/１"
lines_seen = set()
outfile=open(writeDir,"w",encoding="UTF-8-sig")
f = open(readDir,"r",encoding="UTF-8-sig")
for line in f:
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print("success")


