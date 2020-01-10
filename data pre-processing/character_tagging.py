##################

#coding=utf-8

import codecs
import sys

input_data = codecs.open("C:\\Users\\79844\\.anaconda\\demo\\BiGRU\\data\\pos.txt","r",encoding="UTF-8-sig")
output_data = codecs.open("C:\\Users\\79844\\.anaconda\\demo\\BiGRU\\data\\ccks2018.txt","w",encoding="UTF-8-sig")
for line in input_data.readlines():
    word_list = line.strip().split()
    for word in word_list:
        if '/chec' in word:
            if len(word) == 6:
                output_data.write(word[len(word) - 6] + '\t' + 'B-chec' + '\r\n')
            else:
                output_data.write(word[0] + '\t' + 'B-chec'+"\r\n")
                for w in word[1:len(word) - 5]:
                    output_data.write(w + '\t' + 'I-chec' + '\r\n')
                #output_data.write(word[len(word)-6] + '\t' + 'E-chec' + '\r\n')
        else:
            if '/body' in word:
                if len(word) == 6:
                    output_data.write(word[len(word) - 6] + '\t' + 'B-body' + '\r\n')
                else:
                    output_data.write(word[0] + '\t' + 'B-body'+'\r\n')
                    for w in word[1:len(word) - 5]:
                        output_data.write(w + '\t' + 'I-body' + '\r\n')
                    #output_data.write(word[len(word)-6] + '\t' + 'E-body' + '\r\n')
            else:
                if '/dise' in word:
                    if len(word) == 6:
                        output_data.write(word[len(word) - 6] + '\t' + 'B-dise' + '\r\n')
                    else:
                        output_data.write(word[0] + '\t' + 'B-dise'+'\r\n')
                        for w in word[1:len(word) - 5]:
                            output_data.write(w + '\t' + 'I-dise' + '\r\n')
                        #output_data.write(word[len(word)-6] + '\t' + 'E-dise' + '\r\n')
                else:
                    if '/symp' in word:
                        if len(word) == 6:
                            output_data.write(word[len(word) - 6] + '\t' + 'B-symp' + '\r\n')
                        else:
                            output_data.write(word[0] + '\t' + 'B-symp'+'\r\n')
                            for w in word[1:len(word) - 5]:
                                output_data.write(w + '\t' + 'I-symp' + '\r\n')
                            #output_data.write(word[len(word)-6] + '\t' + 'E-symp' + '\r\n')
                    else:
                        if '/cure' in word:
                            if len(word) == 6:
                                output_data.write(word[len(word) - 6] + '\t' + 'B-cure' + '\r\n')
                            else:
                                output_data.write(word[0] + '\t' + 'B-cure'+'\r\n')
                                for w in word[1:len(word) - 5]:
                                    output_data.write(w + '\t' + 'I-cure' + '\r\n')
                                #output_data.write(word[len(word)-6] + '\t' + 'E-cure' + '\r\n')
                        else:
                            for w in word:
                                output_data.write(w + '\t' + 'O' + '\r\n')
    output_data.write('\r\n')
        #if len(word) == 1:
        #else:
            #output_data.write(word[0]+"/B")
            #for w in word[1:len(word)-1]:
                #output_data.write(w+"/M")
            #output_data.write(word[len(word)-1]+"/E")
    #output_data.write("\n")
input_data.close()
output_data.close()

