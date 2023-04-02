# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 21:51:45 2021

@author: neo
菜鸟Python实战-05爬虫之爬取视频
参考内容1：https://blog.csdn.net/weixin_48923393/article/details/117377043?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.control&spm=1001.2101.3001.4242
参考内容2：https://blog.csdn.net/cainiao_python/article/details/117049922?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-18.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-18.control
"""

import requests
from bs4 import BeautifulSoup
import time
import random
import json
import re
from tqdm import tqdm  # 进度条

import urllib.request  # 制定URL，获取网页数据  #另外一种下载视频的方式（方法2）

url_file_name = '.\\Result_File\\url.txt'


def get_list():
    for p in range(1):  # 抓取页数

        html = requests.get('https://v.huya.com/g/pet?set_id=43&order=hot&page={}'.format(p + 1))  # 每一页的网址
        soup = BeautifulSoup(html.text, 'html.parser')
        ul = soup.find('ul', class_='vhy-video-list w215 clearfix')  # 截取页面视频部分内容
        lis = ul.find_all('li')  # 每一个li里面对应一个视频，找到所有的li
        for li in lis:
            a = li.find('a', class_='video-wrap statpid')  # 截取a树状图部分内容
            href = a.get('href')  # 视频子网页的链接地址
            title = a.get('title')  # 视频名字
            # 去掉文件名中的特殊字符
            title = validate_title(title)
            with open(url_file_name, 'a', encoding='utf-8') as f:
                f.write(title + '|' + href + '\n')  # 存入 txt 文本
        print("已经抓取了 {} 页".format(p + 1))
        time.sleep(random.randint(1, 9) / 10)


# 去掉文件名中的特殊字符
def validate_title(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    new_title = re.sub(rstr, "", title)
    return new_title


def get_video_url():
    urls_file = open(url_file_name, 'r', encoding='utf-8')
    url_lines = urls_file.readlines()
    urls_file.close()

    video_urls = []
    for line in tqdm(url_lines, '视频真实播放地址获取中......'):  # 显示读条
        # for line in url_lines:                                     #不显示读条
        # 视频名字 | 地址
        infos = line.split('|')
        video_id = infos[1].replace('.html\n', '').replace('/play/', '')
        data = requests.get(
            'https://v-api-player-ssl.huya.com/?r=vhuyaplay%2Fvideo&vid={}&format=mp4%2Cm3u8'.format(video_id))
        # with open('.\\Result_File\\data.txt','a',encoding = 'utf-8') as f:
        #         f.write(data.text)         #存入 txt 文本  json 格式化后结果
        data = json.loads(data.text)
        url = data['result']['items'][0]['transcode']['urls'][0]  # 视频的真实播放地址
        # print("333")
        # print(url)
        # print("444")
        video_urls.append({'title': infos[0], 'url': url})  # 字典形式写入视频标题及视频的真实播放地址

    return video_urls


def save_video(video_urls):
    for item in tqdm(video_urls, '视频下载中......'):  # 显示读条
        # for item in video_urls:                               #不显示读条
        title = item.get('title')
        print('正在下载：{}'.format(title))
        html = requests.get(item.get('url'))
        data = html.content
        with open('.\\Result_File\\{}.mp4'.format(title), 'wb') as f:
            f.write(data)
            # break   #测试用，加上break只用下载一个视频，缩短debug时间，正常跑请注释掉
    print('全部下载完成了')


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    get_list()
    print("文档获取完毕！")
    video_urls = get_video_url()
    save_video(video_urls)
    print("所有步骤完毕！")

    # 另外一种方法（方法2）
    # imgurl = 'http://videotx-platform.cdn.huya.com/1048585/1199520110371/25830031/67ce11c6ebebe5939871f9584df84840.mp4?bitrate=1084&client=106&definition=1300&pid=1199520110371&scene=vod&vid=548357759'
    # urllib.request.urlretrieve(imgurl, '.\\Result_File\\1.mp4')





