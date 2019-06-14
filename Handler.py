"""
    Handler ：完成复杂的请求，如通过代理请求
"""
import urllib

proxy_handler = urllib.request.ProxyHandler({
    'http': '127.0.0.1:9666'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org')
print(response.read())
