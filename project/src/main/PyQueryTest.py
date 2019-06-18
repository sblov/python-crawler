"""
    PyQuery
    类似Jquery
"""
from pyquery import PyQuery as pq

# 字符串初始化
html = """
<html lang="en">
<body>
    <ul id="u1">
        <li class="l1"><a id="at" href="index.html" class="test">test</a></li>
        <li class="l2"><a id="at1" href="index.html" class="test1">test</a></li>
        <li class="l3"><a id="at2" href="index.html" class="test2">test</a></li>
        <li class="l4"><a id="at3" href="index.html" class="test3">test</a></li>
        <li class="l5"><a id="at4" href="index.html" class="test4">test</a></li>
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
if 1==0:
    doc = pq(filename='./project/src/main/demo.html')
    print(doc('head'))

"""
    基本CSS选择器
"""
doc = pq(html)

if 1==0:    
    print(doc('#u1 li .test'))

    # 子标签
    items = doc('#u1')
    print(type(items))
    # lis = items.find('li')
    # lis = items.children()
    lis = items.children('li .test')
    print(type(lis))
    print(lis)

    # 父标签
    print(type(items.parent()))
    print(items.parent())
    print(items.parents())

    # 兄弟元素
    li = items.find('.l2')
    print(li.siblings())
    print(li.siblings('.l4'))
    
    # 遍历元素 
    for l in items.find('li').items() :
        print(l)

"""
    获取信息
"""
if 1==0:
    a1 = doc('a.test1')
    print(a1)

    # 获取属性
    print(a1.attr('href'))
    print(a1.attr.href)

    # 获取文本
    print(a1.text())

    # 获取html
    print(a1.html())

"""
    DOM操作
"""
if 1==1:
    a1 = doc('a.test1')
    print(a1)
    a1.removeClass('test1')
    print(a1)
    a1.addClass('test1')
    print(a1)

    a1.attr('name', 'link1')
    print(a1)
    a1.css('font-size', '14px')
    print(a1)

    ul = doc('ul')
    ul.find('.l1').remove()
    print(ul)

"""
    其他DOM 
        https://pyquery.readthedocs.io/en/latest/index.html
"""