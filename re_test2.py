import re

# 匹配如下内容：单词+空格+单词+任意字符
m = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
match = m.match('hello world')

if match:
    print(match.groups())