
fp = open("C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例标注\\result.txt","r",encoding='UTF-8-sig')
fout = open('C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例\\dic.txt', 'w',encoding='UTF-8-sig')
str = []
strs = []
for line in fp.readlines():
    for str in line:
        if str=="\t":
            strs.append("\n")
            break
        if not str=="\t":
            strs.append(str)
for line in strs:
    fout.write(line)

print("done")