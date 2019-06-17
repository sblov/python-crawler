"""
    PyQuery
    类似Jquery
"""
from pyquery import PyQuery as pq

# 字符串初始化
html = """
<html lang="en">
<body>
    <ul>
        <li><a href="index.html" class="1">test</a></li>
        <li><a href="index.html" class="1">test</a></li>
        <li><a href="index.html" class="1">test</a></li>
        <li><a href="index.html" class="1">test</a></li>
        <li><a href="index.html" class="1">test</a></li>
    </ul>
</body>
</html>
"""
if 1==0:
    doc = pq(html)
    print(doc('li'))

# url初始化
if  1==0:
    doc = pq('http://www.baidu.com')
    print(doc('head'))

# 文件初始化
if 1==1:
    doc = pq(filename='./project/src/main/demo.html')
    print(doc('head'))
