import time
import selenium
from selenium import webdriver
import json

url = "https://www.csdn.net"
path = r'C:/Users/Win10/Desktop/cookie_date.txt'

with open(path, 'r', encoding='utf-8') as f:
    # for line in f:
    #     keys = line.split("	")[5]
    cookie_date = json.loads(f.read())
    try:
        Edge_options = webdriver.EdgeOptions()
        proxy = 'proxy_ip'
        Edge_options.add_argument('--proxy-server=%s' % proxy)
        Edge = webdriver.Edge(options=Edge_options)
        Edge.get(url)
        Edge.implicitly_wait(30)
        Edge.delete_all_cookies()
        for enum in cookie_date:
            if isinstance(enum.get('expiry'), float):
                enum['expiry'] = int(enum['expiry'])
            Edge.add_cookie(enum)
            Edge.implicitly_wait(30)
        print(cookie_date)
        Edge.implicitly_wait(30)
        Edge.refresh()
        time.sleep(30)
        Edge.quit()
    except:
        print("login_false")
# print(read)
# read=re.findall()
