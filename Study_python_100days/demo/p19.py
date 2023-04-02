import this
'''f1 = open(r"d:\tmp\scott.sql", "r", encoding="UTF-8")
flist = f1.readlines()
f1.close()
print(type(flist))
print(len(flist))
# print(flist)
for line in flist:
    print(line, end="")
    
# open函数，作用是打开一个文件，常用的参数有三个
# 第一个参数，文件的路径及文件名，要在字符串的前面加上r，使用raw_string，以免出现问题
# 第二个参数，打开文件的方式，常用的有三种，r代表读取文件，w代表覆盖写入文件，a代表追加写，把内容跟着原内容的后面
# 第三个参数，是设定文件的字符集，也就是文件所使用的语言，一般情况下，使用UTF-8
# 有一种老式的中文字符集，成为GBK编码

f1 = open(r"d:\Python学习重点.txt", "r", encoding="GBK")

print(f1.read())

import time
n1=0
f1 = open(r"d:\tmp\scott.sql", "r", encoding="UTF-8")

while True:
    n1 += 1
    # readline函数，每次读取一行，然后光标移动到新一行
    line = f1.readline()
    if line:
        print(n1, end="\t")
        print(line, end="")
        # time.sleep(1)
    else:
        # print("line is ", line)
        break
f1.close()
print("===================文件输出完成！===============")
'''