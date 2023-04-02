"""
import os
import time




r = open(r'C:\Users\Administrator\Desktop\test.txt','r',encoding='GBK')
i = 0
while True:
    i += 1
    n = r.readline()
    if n:

        s2 = os.path.join(r'C:\Users\Administrator\Desktop', 'test1.txt')
        with open(s2, 'a', encoding='utf-8') as f:
            f.write(str(i) + n)
    else:
        break

print('保存成功')



# =================== 课后练习 ==========================
def stuAdd():
    name=input("请输入姓名：")
    id=input("请输入学号")
    f=open(r"d:\test.txt","a", encoding="UTF-8")
    f.write("%-13s%-13s\n"%(name,id))
    f.close()
    print("*****添加成功！*****")

def stuSelect():
    f=open(r"d:\test.txt","r", encoding="UTF-8")
    t=f.read()
    f.close()
    print(t)

def stuClear():
    f=open(r"d:\test.txt","w", encoding="UTF-8")
    f.write("%-13s%-13s\n"%("name","id"))
    f.close()
    print("*****学生信息已清空！*****")

while True:
    n=input("1.添加学生信息\n2.查看学生信息\n3.清空学生信息\n4.退出\n请选择：")
    if n=="1":
        stuAdd()
    elif n=="2":
        stuSelect()
    elif n=="3":
        stuClear()
    elif n=="4":
        print("*****再见！*****")
        break
    else:
        print("输入有误 ，请重新选择")


import re
#正则表达式，是一种模式匹配规则，例如邮箱格式验证，身份验证
# 搜索，例如在字符串中进行搜索

# * ?称为通配符, sql % _
# ls *.txt ???.txt

# 被搜索的文本
str2 = "床前明月光，疑是地上霜，举头望明月，低头思故乡"
# # 搜索的关键字
key = r"床前"
# #
# search 第一个参数是关键词，第二个参数是被搜索的内容。
# 如果没有搜索到，返回None
# result = re.search(key, str2)
# result = re.match(key, str2)
result = re.fullmatch(key, str2)
print("任意位置搜索模式：", result)
if result:
    print("搜索成功")
else:
    print("搜索失败，没有结果")
"""




