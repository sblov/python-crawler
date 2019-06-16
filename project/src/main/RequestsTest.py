"""
    Requests是用Python语言编写，基于urllib，采用Apache2 Licensed开源协议的Http库
    比urllib更加方便
    文档 ： https://2.python-requests.org//zh_CN/latest/user/quickstart.html
"""
import requests

# 基本使用
if 1==0 : 
    response = requests.get('http://www.baidu.com')
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(response.cookies)

# 各种请求方式
if 1==0 : 
    requests.get('http://www.baidu.com')
    requests.post('http://httpbin.org/post')
    requests.delete('http://httpbin.org/delete')
    requests.put('http://httpbin.org/put')
    requests.head('http://httpbin.org/get')
    requests.options('http://httpbin.org/get')

"""
    基本GET请求
"""
# 基本写法
if 1==0 : 
    response = requests.get('http://httpbin.org/get')
    response = requests.get('http://httpbin.org/get?name=lov&age=22')

    data = {
        'name': 'lov1',
        'age': 221
    }
    response = requests.get('http://httpbin.org/get', params=data)

    print(response.text)
    # 解析json
    print(response.json())
    print(type(response.json()))

# 获取二进制数据
if 1==0 : 
    response = requests.get('http://github.com/favicon.ico')
    print(type(response.text), type(response.content))
    print(response.content)
    with open('favicon.ico','wb') as f:
        f.write(response.content)
        f.close()

# 添加headers
if 1==0 : 
    response = requests.get('http://www.zhihu.com/explore')
    print(response.text)

    headers = {
        'User-Agent': 'Chrome/73.0.3683.103'
    }
    response = requests.get('http://www.zhihu.com/explore', headers=headers)
    print(response.text)

"""
    基本POST请求
"""
if 1==0:
    data = {
        'name': 'lov',
        'age': 22
    }
    headers = {
        'User-Agent': 'Chrome/73.0.3683.103'
    }
    response = requests.post('http://httpbin.org/post', data=data, headers=headers)
    print(response.text)

"""
    响应
"""
# response属性
if 1==0:
    response = requests.get('http://httpbin.org/get')
    print(type(response.status_code), response.status_code)
    print(type(response.headers), response.headers)
    print(type(response.cookies), response.cookies)
    print(type(response.url), response.url)
    print(type(response.history), response.history)

    exit() if response.status_code != 200 else print('Successful')

    print(type(requests.codes))

"""
    其他
"""
# 文件上传
if 1==0:
    files = {'file': open('favicon.ico', 'rb')}
    response = requests.post('http://httpbin.org/post',files=files)
    print(response.text)

# 获取cookie
if 1==0:
    response = requests.get('http://www.baidu.com')
    print(response.cookies)
    for key, value in response.cookies.items():
        print(key+' : '+value)

# 会话维持
# 默认cookie无法维持会话
if 1==0:
    requests.get('http://httpbin.org/cookies/set/name/lov')
    response = requests.get('http://httpbin.org/cookies')
    print(response.text)
    
# 使用Session对象访问维持会话
if 1==0:
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/name/lov')
    response = s.get('http://httpbin.org/cookies')
    print(response.text)

# 证书验证
if 1==0:
    # 没有安全证书的网址以https访问，会返回ssl异常
    # (Caused by SSLError(SSLCertVerificationError("hostname 'www.scujj.edu.cn' doesn't match 'xxzx.scujj.edu.cn'")
    # response = requests.get('https://www.scujj.edu.cn')
    response = requests.get('https://www.scujj.edu.cn', verify=False)
    print(response.text)

# 代理设置
if 1==0:
    proxies = {
        'https': 'https://127.0.0.1:9666'
    #  'https': 'https://user:password@127.0.0.1:9666'
    # socks代理：pip install 'requests[socks]'
        #   'https': 'socks5://127.0.0.1:9666'
    }
    # HTTP/2.0 只能以https访问
    response = requests.get('https://www.baidu.com', proxies=proxies)
    print(response.status_code)


# 超时设置
if 1==0:
    try:
        response = requests.get('http://httpbin.org', timeout=0.1)
        print(response.text)
    except requests.exceptions.Timeout as  e:
        print('Time Out')

from requests.auth import HTTPBasicAuth
# 认证设置
if 1==1:
    
    # r = requests.get('http://127.0.0.1:8080/manager/status') 
    # r = requests.get('http://127.0.0.1:8080/manager/status', auth=HTTPBasicAuth('admin', 'admin'))
    r = requests.get('http://127.0.0.1:8080/manager/status', auth=('admin', 'admin'))
    print(r.status_code)

# 异常处理
