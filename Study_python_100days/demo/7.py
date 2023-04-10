import requests

url = 'https://www.baidu.com'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
r = requests.get(url=url, headers=headers)
# 打印Cookies对象
print(r.cookies)
# 遍历Cookies
for key, value in r.cookies.items():
	print(key + '=' + value)
# ————————————————
# 版权声明：本文为CSDN博主「上善若水。。」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/m0_43404934/article/details/122331463
