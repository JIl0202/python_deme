from pyquery import PyQuery
import requests
import json
from bs4 import BeautifulSoup

# 1分析目标网站，确定爬取的url路径，headers参数
url = r'https://haokan.baidu.com/videoui/api/videorec?title=%E5%A6%82%E6%9E%9C%E5%9C%B0%E7%90%83%E7%9A%84%E5%A4%A9%E7%84%B6%E5%8D%AB%E6%98%9F%E6%9C%88%E7%90%83%E5%8F%98%E6%88%90%E4%BA%86%E9%87%91%E6%98%9F%EF%BC%8C%E5%B0%86%E4%BC%9A%E5%8F%91%E7%94%9F%E4%BB%80%E4%B9%88%EF%BC%9F&vid=3687686622738524263&act=pcRec&pd=pc'
headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}
# 2发送请求，获取响应数据
rp= requests.get(url, headers=headers)
# response=json.dumps(rp,ensure_ascii=False)
respon=rp.json()
print(respon)



# comments=json.loads(raw_json[20:-2])['play_url']
# comments
# 3解析数据
# 3.1数据转换
# do = json.loads(response)
# print(do)
# 3.2数据解析
# data_list = response['data']['response']['videos']

# for data in data_list:
#       print(data)
#     video_title = data["title"] + ".mp4"  # 视频文件名
#     video_url = data['play_url']  # 视频的url地址
#     # print("视频名称为：{video_title}\nURL地址为：{video_url}".format(video_title=video_title,video_url=video_url))
#
#     # 4保存数据
#     # 再次发送请求
#     print("正在下载：", video_title)
#     video_data = requests.get(video_url, headers=headers)
#     with open(r'F:\papapa\video\' + video_title', 'wb') as f:  # 视频是二进制，所以需要用到wb写入方式
#         f.write(video_data.content)
#         print("下载完成！\n")

