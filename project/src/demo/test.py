from pyquery import PyQuery as pq
import requests
from html.parser import HTMLParser
import re


header = {
    'User-Agent': 'Chrome/75.0.3770.80'
}

html = requests.get('https://www.toutiao.com/group/6704527856690528775/', headers=header)

pattern = re.compile('pgc-img.*?img src&#x3D;&quot;(.*?);', re.S)

urls = re.findall(pattern, html.text)
print(urls)


# html = HTMLParser().unescape('&lt;div&gt;&lt;p&gt;忌安子癌 2019-06-17 13:52&lt;/p&gt;&lt;p&gt;高个子美女穿红色深V连衣裙，气质满满，轻熟气息挡不住！&lt;/p&gt;&lt;div class&#x3D;&quot;pgc-img&quot;&gt;&lt;img src&#x3D;&quot;http://p3.pstatp.com/large/pgc-image/a77ffc0700a846a49c451ef3fdb76cc5&quot; img_width&#x3D;&quot;638&quot; img_height&#x3D;&quot;1077&quot; alt&#x3D;&quot;肤白貌美的美女街拍：富有风韵的美女，穿出东方知性美&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p class&#x3D;&quot;pgc-img-caption&quot;&gt;&lt;/p&gt;&lt;/div&gt;&lt;p&gt;她穿着白色的露肩衣个黑色的超短裙，斜背着一个酒壶形状的包包，看起来特别有特色又别致呢。&lt;/p&gt;&lt;div class&#x3D;&quot;pgc-img&quot;&gt;&lt;img src&#x3D;&quot;http://p3.pstatp.com/large/pgc-image/481c844fc33f40ad8d67b01ea3a3415b&quot; img_width&#x3D;&quot;640&quot; img_height&#x3D;&quot;902&quot; alt&#x3D;&quot;肤白貌美的美女街拍：富有风韵的美女，穿出东方知性美&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p class&#x3D;&quot;pgc-img-caption&quot;&gt;&lt;/p&gt;&lt;/div&gt;&lt;p&gt;吊带长裙外搭针织衫，好身材秀出来，小姐姐两人是同款凉鞋，颜色很俊俏惊艳，视觉效果很不错，日常搭配需要一双这样精致好看的鞋子。&lt;/p&gt;&lt;div class&#x3D;&quot;pgc-img&quot;&gt;&lt;img src&#x3D;&quot;http://p1.pstatp.com/large/pgc-image/21eb418360cc4281bd7a0bbb0bc7bae3&quot; img_width&#x3D;&quot;635&quot; img_height&#x3D;&quot;835&quot; alt&#x3D;&quot;肤白貌美的美女街拍：富有风韵的美女，穿出东方知性美&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p class&#x3D;&quot;pgc-img-caption&quot;&gt;&lt;/p&gt;&lt;/div&gt;&lt;p&gt;在风中，小姐姐头发乱飞，简单干净的着装，给人一种清爽大方的自然之美。&lt;/p&gt;&lt;div class&#x3D;&quot;pgc-img&quot;&gt;&lt;img src&#x3D;&quot;http://p3.pstatp.com/large/pgc-image/1268776db7ad499684b6bbab30c65f88&quot; img_width&#x3D;&quot;640&quot; img_height&#x3D;&quot;855&quot; alt&#x3D;&quot;肤白貌美的美女街拍：富有风韵的美女，穿出东方知性美&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p class&#x3D;&quot;pgc-img-caption&quot;&gt;&lt;/p&gt;&lt;/div&gt;&lt;p&gt;美女穿着白色衬衫去扣纽扣，美丽的身躯是一件漂亮的背黑色大衣，女孩的身体是牛仔面料，短裤、短衬衫和短裤几乎都是长的，所以它绝对是很酷也很勇敢穿的，整体的建设也是一条长长的腿。&lt;/p&gt;&lt;div class&#x3D;&quot;pgc-img&quot;&gt;&lt;img src&#x3D;&quot;http://p3.pstatp.com/large/pgc-image/b2658caca52e493ea4e4b2dca602fbde&quot; img_width&#x3D;&quot;511&quot; img_height&#x3D;&quot;758&quot; alt&#x3D;&quot;肤白貌美的美女街拍：富有风韵的美女，穿出东方知性美&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p class&#x3D;&quot;pgc-img-caption&quot;&gt;&lt;/p&gt;&lt;/div&gt;&lt;p&gt;小姐姐穿棕色吊带配喇叭口牛仔裤，秀出丰满身材&lt;/p&gt;&lt;div class&#x3D;&quot;pgc-img&quot;&gt;&lt;img src&#x3D;&quot;http://p1.pstatp.com/large/pgc-image/e8e65e0b3dff41a8a3aae4175e7429a8&quot; img_width&#x3D;&quot;640&quot; img_height&#x3D;&quot;847&quot; alt&#x3D;&quot;肤白貌美的美女街拍：富有风韵的美女，穿出东方知性美&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p class&#x3D;&quot;pgc-img-caption&quot;&gt;&lt;/p&gt;&lt;/div&gt;&lt;p&gt;街拍：熟女穿红色连衣裙，侧身都这么有魅力！&lt;/p&gt;&lt;div class&#x3D;&quot;pgc-img&quot;&gt;&lt;img src&#x3D;&quot;http://p3.pstatp.com/large/pgc-image/52aa4c8ea2aa48c180b24fdc3efa28fa&quot; img_width&#x3D;&quot;640&quot; img_height&#x3D;&quot;902&quot; alt&#x3D;&quot;肤白貌美的美女街拍：富有风韵的美女，穿出东方知性美&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p class&#x3D;&quot;pgc-img-caption&quot;&gt;&lt;/p&gt;&lt;/div&gt;&lt;p&gt;（以上图片均来自网络）&lt;/p&gt;&lt;/div&gt;')

# doc = pq(html)

# doc('')