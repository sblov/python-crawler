"""
    Handler ：完成复杂的请求，如通过代理请求
"""
import requests
# import urllib.request as req

# proxy_handler = req.ProxyHandler({
#     'http': '106.75.140.78:8888'
# })
# opener = req.build_opener(proxy_handler, )
# response = opener.open('http://javbx.com/casts/prefix/A/1.html')
# print(response.read())


header = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':
    'gzip, deflate',
       'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48 (Edition B2)'
}
proxies = {'http': '163.125.75.104:9797', }
url = "http://javbx.com/casts/prefix/A/1.html"

response = requests.get(url, headers=header, proxies=proxies, timeout=20)
print(response.status_code)
# print(type(response.text))
print(response.text)
# print(response.cookies)