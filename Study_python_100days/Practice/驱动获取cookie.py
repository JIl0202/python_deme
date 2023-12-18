import selenium
from selenium.webdriver.edge import webdriver
import json
import time

### 下面是chromedriver路径，自己填
Edge = selenium.webdriver.Edge()
### 打开要自动登录的网站，比如说csdn
Edge.get("https://www.csdn.net/")
###手动完成登录后，随便在控制台输入内容，就保存下来了
input("等待登录成功，登录成功后随便输入内容。")
dictCookies = Edge.get_cookies()
jsonCookies = json.dumps(dictCookies)

with open('c:/Users/win10/Desktop/cookie_date.txt', 'w') as f:
    f.write(jsonCookies)

print('cookies保存成功！')