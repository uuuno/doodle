# -*- coding:utf-8 -*-
n = int(input())
loss = 2025 - n
for i in range(1,10):
    if i*9 < loss:
        continue
    else:
        for j in range(1,10):
            if i*j == loss:
                print(i, 'x', j)
