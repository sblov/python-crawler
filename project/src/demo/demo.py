import requests
from bs4 import BeautifulSoup as bs
from pyquery import PyQuery as pq
from selenium import webdriver
import re

headers = {
        'User-Agent': 'Chrome/73.0.3683.103'
}
# response = requests.get('https://www.wegame.com.cn/platform/article/detail.html?feedsid=6bfcf9352ab34e5ba1c8df310c1c6a59&articleId=9215a95c63d34f86871d08ddc4c2e4e9', headers=headers)

browser  = webdriver.Chrome()
browser.get('https://www.wegame.com.cn/platform/article/detail.html?feedsid=6bfcf9352ab34e5ba1c8df310c1c6a59&articleId=9215a95c63d34f86871d08ddc4c2e4e9')

# print(browser.page_source)

doc = pq(browser.page_source)

imgs = doc('img').items()
print(imgs)


pattern = re.compile(r'[\w]{12,}')

for img in imgs:
    print(img.attr('src'))
    response = requests.get(img.attr('src'))
    # print(type(response.text), type(response.content))
    # print(response.content)
    file_name = pattern.findall(img.attr('src'))[0]+'.png'
    print(file_name)
    with open(file_name,'wb') as f:
        f.write(response.content)
        f.close()