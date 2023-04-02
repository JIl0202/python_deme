import requests

url = "https://www.zhihu.com"
headers ={

'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

'Cache-Control':'max-age=0',

'Connection':'keep-alive',

'Referer':'http://www.baidu.com/',

'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'}
R = requests.get(url,headers=headers)
w = open('C://Users//Administrator//Desktop//test.txt','a',encoding='UTF-8')
print(w.write(R.text))