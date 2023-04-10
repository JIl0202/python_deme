import sys

flag = False
try:
    path = input("输入一个文件名：")
    f1 = open(path, "r", encoding="GBK")

    print(f1.read())
    flag = True
except:
    print(sys.exc_info())
    print("文件打开出错")

if flag:
    print("文件读取完成")

"""

#程序出错，抛出异常 exception，如果没有捕获异常，那么程序将崩溃
# python语言用try...except...结构处理异常
# 那些典型的场景需要用try...except...处理
# 1. 用户输入，2. 函数参数检查，3. 文件处理，文件读写，4. 网络传输，网络请求，5. 数据库处理
# 6. 自动化测试

# 在 Python 中，把程序运行时产生错误的情况叫做异常。出现异常情况有很多，常见的异常有以下几种：
# AssertionError    断言语句失败（assert 后的条件为假）
#
# AttributeError    访问的对象属性不存在
#
# ImportError    无法导入模块或者对象，主要是路径有误或名称错误
#
# IndentationError 代码没有正确对齐，主要是缩进错误
#
# IndexError    下标索引超出序列范围
#
# IOError        输入/输出异常，主要是无法打开文件
#
# KeyError    访问字典里不存在的键
#
# NameError     访问一个未声明的变量
#
# OverflowError    数值运算超出最大限制
#
# SyntaxError    python语法错误
#
# TabError    Tab和空格混用
#
# TypeError    不同类型数据之间的无效操作（传入对象类型与要求的不符合）
#
# ValueError    传入无效的值，即使值的类型是正确的
#
# ZeroDivisionError    除法运算中除数0 或者 取模运算中模数为0
#
# 一旦程序发生异常，表明该程序在执行时出现了非正常的情况，无法再执行下去。默认情况下，程序会终止退出。

import re

email1 = "micsoft@outlook.cn"
email2 = "meteoren@163.com"
email3 = "abcddd264.ccab"
email4 = "@.com"
elist = [email1,email2,email3,email4]

emailreg = '\w{3,12}@\w{3,12}\.\w{2,4}'

ereg = re.compile(emailreg)

for i in elist:
    if re.fullmatch(ereg,i):
        print('匹配成功', end = '\t')
    else:
        print('匹配失败', end = '\t')

# 异常捕获机制，try...except
try:
    age = int(input("请问贵庚: "))
    print(age)
    print("今年：%d 岁" % age)
except:
    print("请输入数字")


print("程序结束！")

list = ['王五','张三','李四','王麻子']

result = re.search(r'\w{2}', str(list))

print('结果为',result)


print("==========自制grep命令==============")
key = input("请输入搜索的关键词：")
file1 = input("请输入搜索的文件名：")
f1 = open(file1, "r", encoding="GBK")
# f1 = open(r"d:\tmp\scott.sql", "r", encoding="UTF-8")
flist = f1.readlines()
f1.close()

flag = True
n = 0
for line in flist:
    # re.I，搜索时忽略大小写
    n += 1
    r1 = re.search(key, line, re.I)
    if r1:
        print("搜索成功，在第%d行，关键词是: %s，内容是：%s" % (n, key, line), end="")
        flag = False

if flag:
    print("没搜到")
    

邮箱的规则，开头有若干个字母和数字，后面接一个@符号
@后面，应该是一个域名：有若干个字母和数字，接一个.号
.号的后面有2~4个字母数字的域名后缀


import re

# emailreg = "[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]{2,4}"
emailreg = "\w+@\w+\.\w{2,4}"
email1 = "mi@oksugar.cn"
email2 = "meteoren@163.com"
email3 = "abcddd264.ccab"
email4 = "@.com"


# 编译模板字符串，检查正则表达式语法规则是否正确
ereg = re.compile(emailreg)
print(type(ereg))

if re.fullmatch(ereg, email1):
    print("匹配成功！")
else:
    print("匹配失败")
"""
