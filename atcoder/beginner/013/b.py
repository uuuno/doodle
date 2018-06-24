# -*- coding:utf-8 -*-
a = int(input())
b = int(input())
print(min([abs(b-a), abs(b+10-a), abs(b-10-a)]))
