from selenium import webdriver
from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests
from selenium.webdriver.support.wait  import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import re
from mgconfig import * 
import pymongo
import time
import json

client = pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

img_index = 10

def get_page_index(key):
    browser = webdriver.Chrome()

    browser.get('https://www.toutiao.com/search/?keyword='+key)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'img-close')))
    browser.find_element_by_id('img-close')

    browser.get('https://www.toutiao.com/search/?keyword='+key)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'J_section_1')))

    return browser.page_source

def parse_page_index(doc):
    items = doc('.img-wrap').items()
    for item in items:
        yield str(item.attr('href'))

def get_subPage_detail(href):
    header = {
    'User-Agent': 'Chrome/75.0.3770.80'
    }
    html = requests.get('https://www.toutiao.com'+href, headers=header)
    pattern = re.compile('pgc-img.*?img src&#x3D;&quot;(.*?)&quot;', re.S)
    urls = re.findall(pattern, html.text)
    for url in urls:
       yield url

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('save success!',result)
        return True
    return False

def write_to_file(content):
    response = requests.get(content)
    
    pattern = re.compile(r'[\w]{12,}')
    file_name = pattern.findall(content)[0]+'.png'

    with open(file_name,'wb') as f:
        f.write(response.content)
        f.close()
def main():
    main_doc = get_page_index('表情包')
    doc = pq(main_doc)
    for url in parse_page_index(doc):
        for result in get_subPage_detail(url):
            print(result)
            write_to_file(result)
            time.sleep(1)


        
    
if __name__ == "__main__":
    main()