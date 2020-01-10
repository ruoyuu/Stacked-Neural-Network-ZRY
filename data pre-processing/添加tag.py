import os
f1 = open('F:\\数据\\train_data600\\病例\\result.txt', 'r', encoding='UTF-8-sig')
fout = open("F:\\数据\\train_data600\\RES.txt","w",encoding="UTF-8-sig")
lines1 = f1.readlines()
path = "F:\\数据\\train_data600\\病例标注\\" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
#def tokenizer(s,x,y):
for file, line1 in zip(files, lines1):
    f2 = open(path + "/" + file, 'r', encoding='UTF-8-sig');
    iter_f = iter(f2)
    lines2 = iter_f.readlines()
    line1 = line1.strip()
    for i in range(len(line1)):
        for line2 in lines2:
            line2 = line2.strip().split()
            a = int(line2[1])
            b = int(line2[2])
            if i == a:
                fout.write(' ')
            if i == b:
                fout.write('/'+line2[3]+' ')
        fout.write(line1[i])
    fout.write('\n')

