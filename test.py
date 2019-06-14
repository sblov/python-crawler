import urllib
import urllib.request
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import  pymysql

print(urllib.request.urlopen('http://www.baidu.com'))

print(requests.get('http://www.baidu.com'))
# ============================================================================
# 创建浏览器驱动，用指定浏览器驱动，打开浏览器，渲染获取到的js/html/css文件
# brower = webdriver.Chrome()
# brower = webdriver.PhantomJS()

# 获取访问网站资源
# brower.get('http://www.baidu.com')

# 获取资源的页面源文件内容
# print(brower.page_source)
# ============================================================================

# =============bs4====================
soup = BeautifulSoup('<html><body></body></html>','lxml')
print(soup)

# ==============PyQuery==================
doc = pq('<html>Html</html>')
print(doc('html').text())

# ==============pymysql=================
conn = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='mysql')
cursor = conn.cursor()

cursor.execute('SELECT * FROM DB')

print(cursor.fetchall())