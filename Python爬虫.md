# Python爬虫

## 环境

> **Python+Pip**、**MongoDB、Redis、Mysql**

## 基本原理

**获取数据**

> 网页文本、图片、视频、其他

**解析方式**

> 直接处理、Json解析、正则表达式、BeautifulSoup、PyQuery、XPath

**javascript渲染问题**

> 分析Ajax请求、Selenium/WebDriver、Splash、PvV8、Ghost.py

**数据保存**

> 文本、关系型数据库、非关系型数据库、二进制文件

## 常用库

> **urllib**、**requests**、**selenium**、**phantomjs**、**lxml**、**beautifulsoup4**、**pyquery**、**pymysql**、**pymongo**、**redis**、**flask**、**django**、**jupyter**

### Urllib

​	Python内置的HTTP请求库

| 模块               | 含义               |
| ------------------ | ------------------ |
| urllib.request     | 请求模块           |
| urllib.error       | 异常处理模块       |
| urllib.parse       | url解析模块        |
| urllib.robotparser | robots.txt解析模块 |

![1560408791889](./img/1560408791889.png)

### Requests

### Selenium

### BeautifulSoup

#### 解析库

| 解析器          | 使用                                | 优势                                                      | 劣势                        |
| --------------- | ----------------------------------- | --------------------------------------------------------- | --------------------------- |
| Python标准库    | BeautifulSoup(markup,'html.parser') | Python内置标准库、执行速度适中、文档容错能力强            | python3.2以前版本中文容错差 |
| lxml html解析器 | BeautifulSoup(markup,'lxml')        | 速度快、文档容错强                                        | 需要安装C语言库             |
| lxml xml解析器  | BeautifulSoup(markup,'xml')         | 速度快、唯一支持xml的解析器                               | 需要安装C语言库             |
| html5lib        | BeautifulSoup(markup,'html5lib')    | 最好的容错性、以浏览器的方式解析文档、生存html5格式的文档 | 速度慢、不依赖外部扩展      |

> - 推荐使用lxml解析库，必要时使用html.parser
> - 标签选择筛选功能弱，但速度快
> - 建议使用find() 、find_all()查询匹配单个结果或多个结果
> - 如果对CSS选择器熟悉建议使用select()
> - 记者常用的获取属性与文本值的方法、



## 国内镜像

windows下： 新建`C:\Users\Administrator\pip\pip.ini`，填写下面内容，保存即可

```shell
[global]  
index-url=http://mirrors.aliyun.com/pypi/simple/  
[install]  
trusted-host=mirrors.aliyun.com  
```

