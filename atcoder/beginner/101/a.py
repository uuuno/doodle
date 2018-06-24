# -*- coding:utf-8 -*-
s = list(input())
m = 0
for i in s:
    if i == '+':
        m += 1
    else:
        m -= 1
print(m)
