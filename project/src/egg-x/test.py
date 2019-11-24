from html.parser import HTMLParser
import html

print(HTMLParser().unescape('''<img src="http://img.netbian.com/file/2019/1118/smallaaddbc1e9630fe52d9938192f610d0f71574079209.jpg" alt="&#x7535;&#x5F71;&#x5C0F;&#x4E11;&#x58C1;&#x7EB8;"/>'''))


print(html.unescape('''<img src="http://img.netbian.com/file/2019/1118/smallaaddbc1e9630fe52d9938192f610d0f71574079209.jpg" alt="&#x7535;&#x5F71;&#x5C0F;&#x4E11;&#x58C1;&#x7EB8;"/>'''))
