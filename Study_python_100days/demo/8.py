# 导包
from time import sleep
import requests
import os
from bs4 import BeautifulSoup
# import re
import urllib3

# 忽略SSL报错
urllib3.disable_warnings()
# 网站路径
url = r'https://quanxiaoshuo.com/157739/'
# 伪装请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
# 发送请求
res = requests.get(url, headers=headers, verify=False)
# 设置编码
res.encoding = 'gbk'
# 使用BeautifulSoup解析页面,选择html.parser解析器
soup = BeautifulSoup(res.text, 'html.parser')
# 得到作者和书名 通过select查询
book_info = soup.select('body > div.text.t_c > h1 > a:nth-child(1) ,body > div:nth-child(3) > div.f_l.t_c.w2 > a')
book_name = book_info[0].text
book_author = book_info[1].text
# print(book_author)
# 设置保存路径
root_path = os.path.abspath(os.path.dirname(__file__))  # 得到当前文件路径
save_path = os.path.join(root_path, book_name + '.txt')

# 取得章节
chapters = soup.select('a')  # 查找a标签,获得章节信息
# print(chapters)
# print(type(chapters))
# print(chapters)
# 章节编号
# list_num = re.findall(r'\d{8}.', str(chapters))
# # 打印章节编号
# print(len(list_num))

# 循环打印
# 打印章节名和连接地址
# for chapter in chapters:
#     print(chapter.text,chapter['href'])
# 定义一个方法得到具体章节的内容
# 定义一个变量判断是爬取此章节
isreq = True
def content(url_last):
    # 当前章节的url等于书籍的url加上章节a标签的href
    global url, headers, isreq
    if isreq:
        # 判断是否到第一章了
        if '第一章' in str(url_last):
            isreq = False
        else:
            return
    url_now = r'https://quanxiaoshuo.com/' + url_last['href']
    print(url_now)
    # 爬取具体章节内容
    res_chap = requests.get(url_now, headers=headers, verify=False)
    res_chap.encoding = 'gbk'
    soup = BeautifulSoup(res_chap.text, 'html.parser')
    cont1 = soup.select('.t_c')
    cont = soup.select('#content')
    sleep(1)
    # 使用一个变量来储存单章内容，第1行是文章标题
    con = '\n' + str(cont1) + '\n'
    print(con)
    # 处理文章内容 soup的select方法返回的是一个列表，所以cont[0]才是我们想要的具体内容，使用for循环得到每一行
    for text in cont[0]:
        # 去除换行标签
        if str(text) == '<br/>':
            con += '\n'
        else:
            con += text.text
    return con

# 定义保存文件的方法
# 首先写入书名和作者
with open(save_path, 'w', encoding='utf-8') as w:
    w.write(book_name + '\n' + book_author)

def save_book(content):
    if content == None:
        return
    with open(save_path, 'a', encoding='utf-8') as f:
        f.write(content)

# 循环章节列表爬取并保存
for chapter in chapters:
    cont = content(chapter)
    save_book(cont)
