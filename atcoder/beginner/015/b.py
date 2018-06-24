# -*- coding:utf-8 -*-
import math
n = int(input())
bugs = list(map(int, input().split()))
sum = 0
count = 0
for i in range(n):
    if bugs[i] != 0:
        sum += bugs[i]
        count += 1
print(math.ceil(sum/count))
