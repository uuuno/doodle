# -*- coding:utf-8 -*-
n, m = map(int, input().split())
imos = [0]*(m+2)
score = 0
for i in range(n):
    l,r,s = map(int, input().split())
    imos[l] += s
    imos[r+1] -= s
    score += s

for i in range(m+1):
    imos[i+1] += imos[i]

imos = imos[1:m+1]
print(score - min(imos))
