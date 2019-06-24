import requests
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import time
import json
import re

def write_to_file(content):
    with open('toutiao.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()

browser = webdriver.Chrome()

browser.get('https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D')

wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_all_elements_located((By.ID, 'img-close')))

img_close = browser.find_element_by_id('img-close')

# time.sleep(2)

browser.get('https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D')
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_all_elements_located((By.ID, 'J_section_1')))

# time.sleep(2)

doc = pq(browser.page_source)

items = doc('.img-wrap').items()

for item in items:
    header = {
    'User-Agent': 'Chrome/75.0.3770.80'
    }

    html = requests.get('https://www.toutiao.com'+str(item.attr('href')), headers=header)

    pattern = re.compile('pgc-img.*?img src&#x3D;&quot;(.*?)&quot;', re.S)

    urls = re.findall(pattern, html.text)

    for url in urls:
        write_to_file(url)

    # html = pq(html.text)
    # print(html)
    # imgs = html('.pgc-img').items()
    # print(imgs)
    # for img in imgs:
    #     print(img.text())

    #     # print(img.attr('src'))

