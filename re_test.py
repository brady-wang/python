import re

pattern = re.compile(r'\d+\.\d*')

match1 = pattern.match('24234')
match2 = pattern.match('432,234')
match3 = pattern.match('2342.242')

if match1 :
    print(match1.group())
else :
    print("match1 匹配失败");

if match2:
        print(match2.group())
else:
        print("match1 匹配失败");

if match3:
    print(match3.group())
else:
    print("match3 匹配失败");