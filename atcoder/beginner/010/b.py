# -*- coding: utf-8 -*-
n = int(input())
flowers = list(map(int, input().split()))
m = 0
for i in range(n):
    flower = list(range(1,flowers[i]+1))
    flower.reverse()
    for j in flower:
        if j%3 !=2 and j%2!=0:
            break
        else:
            m += 1
print(m)
