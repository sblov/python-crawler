import requests
from bs4 import BeautifulSoup as bs
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

browser = webdriver.Chrome()
browser.get('https://movie.douban.com/explore#!type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0')

wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'more')))
# print(browser.page_source)
more = browser.find_element_by_class_name('more')
for i in range(4) :
    more.click()
    time.sleep(1)
doc = pq(browser.page_source)
list = doc('.cover-wp').items()
print(list)

for li in list:
    print('img:', li.children('img').attr('src'), 'name:', li.children('img').attr('alt'))