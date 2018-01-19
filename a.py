#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import math
L = ['a','b','c']
L.append('e')
L.insert(0,'0')
L.pop(-1)
L.append(['dddd','ggggggg'])

T = (1,2,3)

age = 30;
if(age < 10) :
    print('111111111')
elif(age <20):
    print("3333333333333")
elif(age < 30):
    print("444444444")
else:
    print(555555)


L = range(101)
sum = 0
for l in L:
    sum += l;
print(sum)

d = {"name":"wang","age":"28"}
d['test'] = 'test'
d.pop('name')
s = set([1,2,2,3,4])
s.add(5)
s.remove(5)

def my_abs(x,y):
    if x > y :
        return x
    else:
        return y

print(my_abs(1,2))