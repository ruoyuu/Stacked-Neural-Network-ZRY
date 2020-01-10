# -*- coding:utf-8*-
import sys
import importlib
importlib.reload(sys)
import os
import os.path
import time
time1 = time.time()
def MergeTxt(filepath,outfile):
    k = open(filepath+outfile, 'a+', encoding="UTF-8-sig")
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent, filepath)
            f = open(txtPath, encoding = "utf-8")
            k.write(f.read())
            k.write('\n')

    k.close()
    print("finished")
if __name__ == '__main__':
    filepath="F:\\数据\\train_data600\\病例\\"
    outfile="result.txt"
    MergeTxt(filepath,outfile)
    time2 = time.time()
    print(u'总共耗时：' + str(time2 - time1) + 's')
