#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from pyquery import PyQuery as pq
import html as hp
import json

def write_to_file(content):
    with open('./porncover.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()

header = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':
    'gzip, deflate',
       'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48 (Edition B2)'
}
proxies = {'http': '163.125.75.104:9797', }
url = "http://javbx.com/cast/223/azusa-oto.html"

response = requests.get(url, headers=header, proxies=proxies, timeout=20)
response.encoding = response.apparent_encoding
html = response.text

print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)

dom = pq(html)
img_list = dom('#content img').items()

# 判断是否为最后节点
print(dom('.pagination li:last-child') == dom('.pagination .active'))

for img in img_list:
    img_src = hp.unescape(str(img.attr('data-src')))
    img_alt = hp.unescape(str(img.attr('alt')))
    # print('img_src:'+img_src+', img_alt:'+img_alt)
    write_to_file('img_src:http://javbx.com'+img_src+', img_alt:'+img_alt)
