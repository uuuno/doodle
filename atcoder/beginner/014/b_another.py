# -*- coding:utf-8 -*-
n, x = map(int, input().split())
prices = list(map(int, input().split()))
res = 0
i = 0
while x != 0:
    if x & 1:
        res += prices[i]
    i += 1
    x >>= 1
print(res)
