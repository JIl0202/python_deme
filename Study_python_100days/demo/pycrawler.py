'''
乐文小说网
从网页上爬取小说
JIl0202
2022年9月10日00:30:24
'''
# 导包
import requests
from bs4 import BeautifulSoup
import os


url_1 = r'https://www.lewen.club/novel_reading/chapterList?bookid=16072430&sourceid=2457&sort=8'
headers_1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}
res_1 = requests.get(url_1,headers = headers_1)
res_1.encoding = 'ASCii'
soup_1 = BeautifulSoup(res_1.text, 'html')
print(soup_1)
def crawler(num):
    # 请求网址
    url = r'https://www.lewen.club/novelchapter-16072430/%d.html' % num
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
    }
    # 发送请求
    res = requests.get(url, headers=headers)
    # 设置编码
    res.encoding = 'UTF-8'
    # 解析网页源码
    soup = BeautifulSoup(res.text, 'html.parser')
    # 获取标题
    title = soup.select('h1')
    # 获取章节内容
    book = soup.select('.content')
    # 标题打印出来 以便查看爬取进度
    title_1 = '\n' + str(title) + '\n'
    print(title_1)
    # 便利文本内容
    for txt_1 in book:
        txt_2 = '\n%d' % n
        txt_2 += txt_1.text
    return txt_2


# 设置保存路径和保存名称
root_path = r"C:\Users\Win10\Desktop"
save_path = os.path.join(root_path, '物价贬值十亿倍，我成了神豪.txt')


# 保存文本
def save_book(crawler):
    if crawler == None:
        return
    with open(save_path, 'a', encoding='UTF-8') as f:
        f.write(crawler)


# 开始循环打印
for n in range(0, 6579):
    num = 2000198
    num += n
    txt = crawler(num)
    save_book(txt)
