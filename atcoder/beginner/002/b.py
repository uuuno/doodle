# -*- coding:utf-8 -*-
targets = ['a', 'i', 'u', 'e', 'o']
str = input()
for target in targets:
    str = str.replace(target, '')
print(str)
