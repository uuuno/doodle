# -*- coding:utf-8 -*-
data = []
for i in range(4):
    data.append(input().split())
data.reverse()
for row in data:
    row.reverse()
    print(' '.join(row))
