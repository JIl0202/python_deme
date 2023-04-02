 # 语音播放库
import requests
from lxml import etree
# 城市
city = 'wuhan'
# 目标网址
url = 'https://www.tianqi.com/%s/'%city
# 请求头，伪装成浏览器
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
# 向网址发送请求并获取数据
response = requests.get(url=url,headers=headers)
print(response.text)
# 筛选信息
data = etree.HTML(response.text)
weather_list =  data.xpath('//dl[@class="weather_info"]//text()')
print(weather_list)

# 将主要的信息拼在一起,即拼接成一个字符串
weather_text = ''
for text in weather_list:
    weather_text +=text
# 用空格替换掉字符
weather_text = weather_text.replace('[切换城市]',' ')
print(weather_text)
