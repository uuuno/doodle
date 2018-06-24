# -*- coding:utf-8 -*-
import numpy as np
n = int(input())
result = np.zeros(1000001, dtype=int)
for i in range(n):
    a, b = map(int, input().split())
    result[a:b+1] += 1
print(max(result))
