"""
    BeautifulSoup
    灵活又方便的网页解析库，处理高效，支持多种解析器。利用它不用编写正则表达式即可方便实现网页信息的提取
"""
from bs4 import BeautifulSoup

# 基本使用
html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document
"""
soup = BeautifulSoup(html, 'lxml')

if 1==0:
    
    print(soup.prettify())
    print(soup.title.string)

"""
    标签选择器
"""
# 选择元素
if 1==0:
    print(soup.title)
    print(type(soup.title))
    print(soup.head)
    print(soup.meta)

# 获取属性
if 1==0:
    print(soup.meta.attrs['charset'])
    print(soup.meta['charset'])

# 获取内容
if 1==0:
    print(soup.title.string)


# 嵌套选择
if 1==0:
    print(soup.html.head.title.string)

# 子节点与子孙节点
if 1==0:
    print(soup.head.contents)

    print(soup.head.children)
    for i, child in enumerate(soup.head.children):
        print(i, child)

    print(soup.head.descendants)
    for i, child in enumerate(soup.head.descendants):
        print(i, child)

# 父节点与祖先节点
if 1==0:
    # 父节点
    print(soup.meta.parent)
    # 祖先节点
    print(list(enumerate(soup.meta.parents)))

# 兄弟节点
if 1==0:
    print(list(enumerate(soup.meta.next_siblings)))
    print(list(enumerate(soup.meta.previous_siblings)))

"""
    标准选择器
    find_all(name, attrs, recursive, text, **kwargs)
    根据标签名、属性、内容查找文档
"""
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

    <ul>
        <li><a href="index.html" class="test1">test</a></li>
        <li><a href="index.html" class="test2">test</a></li>
        <li><a href="index.html" class="test3">test</a></li>
        <li><a href="index.html" class="test4">test</a></li>
        <li><a href="index.html" class="test5">test</a></li>
    </ul>
    <ul>
        <li><a href="index1.html" class="test21">test2</a></li>
        <li><a href="index1.html" class="test22">test2</a></li>
        <li><a href="index1.html" class="test23">test2</a></li>
        <li><a href="index1.html" class="test24">test2</a></li>
        <li><a href="index1.html" id='aa' class="25">test2</a></li>
    </ul>
</body>
</html>
"""
soup = BeautifulSoup(html, 'lxml')

if 1==0:
    print(soup.find_all('ul'))
    print(type(soup.find_all('ul')[0]))

    for ul in soup.find_all('ul'):
        print(ul.find_all('li'))
    # 属性
    print(soup.find_all(attrs={'class': 1}))
    # 对于特殊属性，直接使用，由于class为关键字，所以使用class_
    print(soup.find_all(class_=1))
    print(soup.find_all(attrs={'href': 'index.html'}))

    # 内容查找
    print(soup.find_all(text='test'))

"""
    find(.....) 
        find返回单个元素，find_all返回所有元素

    find_next_siblings() find_next_sibling()
        返回后面所有兄弟节点 / 返回后面第一个兄弟节点

    find_previous_siblings() find_previous_sibling()
        返回前面所有兄弟节点 / 返回前面第一个兄弟节点

    find_all_next() find_next()
        返回后面所有符合条件的节点 / 返回后面第一条符合条件的节点

    find_all_previous() find_previous()

"""

"""
    CSS选择器
"""
print(soup.select('.test1'))
print(soup.select('ul li'))
print(soup.select('#aa'))
print(type(soup.select('ul')[0]))
for a in soup.select('ul li a'):
    # 内容
    print(a.get_text())
    print(type(a))
    # 属性
    print(a['href'])
    print(a.attrs['class'])

