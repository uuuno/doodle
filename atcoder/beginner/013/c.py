# -*- coding:utf-8 -*-
n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())
cost = a * n
for i in range(n+1):
    y = max(0, (e*(n-i)-h-b*i)//(d+e)+1)
    if y+i <= n:
        cost = min(cost, a*i+c*y)

print(cost)
