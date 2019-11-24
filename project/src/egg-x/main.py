#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from pyquery import PyQuery as pq
import html as hp
import json


def write_to_file(path, content):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def img_src(url):
    header = {
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':
        'gzip, deflate',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48 (Edition B2)'
    }
    proxies = {
        'http': '163.125.75.104:9797',
    }

    # 设置代理请求，20s超时
    response = requests.get(url, headers=header, proxies=proxies, timeout=20)
    # 防止中文乱码
    response.encoding = response.apparent_encoding
    html = response.text

    # 如果非200，终止
    print(response.status_code)
    if response.status_code != 200:
        pass

    # 转PyQuery，方便节点查询
    dom = pq(html)

    # 查询节点， 遍历写入文件
    img_list = dom('#main .list img').items()
    for img in img_list:
        img_src = hp.unescape(str(img.attr('src')))
        img_alt = hp.unescape(str(img.attr('alt')))
        write_to_file('./wallpaper.txt',
                      'img_src:' + img_src + ', img_alt:' + img_alt)

if __name__ == "__main__":
    img_src('http://www.netbian.com/index_10.htm')