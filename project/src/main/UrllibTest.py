"""
    urllib.request.urlopen()函数用于实现对目标url的访问。
    函数原型如下：urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)　
"""

import urllib.request
import urllib.error
import urllib.parse
import socket
import http.cookiejar

# 普通请求
response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# 模拟get与post请求
data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read())

# 模拟超时
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT !!!!')

# 响应类型、状态码、响应头
response = urllib.request.urlopen('http://httpbin.org')
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

"""
    urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
    抽象的URL请求
"""

# 基本使用
request = urllib.request.Request('http://httpbin.org')
response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 设置请求头数据，post请求
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Chrome/73.0.3683.103',
    'Host': 'httpbin.org'
}

dicts = {
    'name': 'China'
}

data = bytes(urllib.parse.urlencode(dicts), encoding='utf8')

req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
# print(response.read())

# 设置请求头数据，post请求
req = urllib.request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Chrome/73.0.3683.103')
response = urllib.request.urlopen(req)
# print(response.read())


"""
    Handler ：完成复杂的请求，如通过代理请求
"""
# 代理
# proxy_handler = urllib.request.ProxyHandler({
#     'http': '127.0.0.1:9666'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org')
# print(response.read())

# Cookie
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
# for item in cookie:
    # print(item.name+'='+item.value)

# 保存cookie
filename = 'Cookie.txt'
# cookie存储格式
cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 读取cookie，什么格式存，就用什么格式读
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('Cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')


"""
    异常处理
"""
try:
    response = urllib.request.urlopen('http://www.cuiqingcai.com/index.htm')
except urllib.error.HTTPError as e:
    print(type(e.reason))
    print(e.reason, e.code, e.headers, sep='\n')
except urllib.error.URLError as e:
    print(e.reason)

"""
    URL解析
"""
# urlparse
result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

result = urllib.parse.urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https', allow_fragments=False)
print(result)

# urlunparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urllib.parse.urlunparse(data))

# urljoin
print(urllib.parse.urljoin('http://www.baidu.com', 'index.html'))
print(urllib.parse.urljoin('http://www.baidu.com', 'https://httpbin.org?org=1'))
print(urllib.parse.urljoin('www.baidu.com', '?cat=2#comment'))
print(urllib.parse.urljoin('www.baidu.com#comment', '?cat=1'))

# urlencode
params = {
    'name': 'lov',
    'age': '22'
}
base_url = 'http://www.baidu.com?'
url = base_url + urllib.parse.urlencode(params)
print(url)
