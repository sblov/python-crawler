import requests
from pyquery import PyQuery as pq

# 获取相应页面
def getPageView(pageUrl):
    
    response = requests.get(pageUrl)
    # 判断返回http状态
    if response.status_code == 200 :
        return response.text
    else:
        return ''

# 获取关键信息
def getKeyContent(content):
    doc = pq(content)
    thumbList = doc('div.item-thumb').items()
    l = []

    for thumb in thumbList:
        d = {}
        d['title']=thumb.children('a').children('img').attr('alt')
        d['img'] = thumb.children('a').children('img').attr('src')
        d['page'] = thumb.children('a').attr('href')
        d['des'] = thumb.children('a').attr('title')
        l.append(d)
        # print(len(l))
        
    return l
        
def init(pageUrl):
    # https://facejav.com/page/2/
    # pageUrl = 'https://facejav.com'
    pageContent = getPageView(pageUrl)
    return getKeyContent(pageContent)