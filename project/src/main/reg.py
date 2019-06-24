import re

pattern = re.compile(r'[\w]{12,}')

m = pattern.findall("aaa---dwedeedwfdwf123223423545")[0]+'.png'

print(m)