# -*- coding:utf-8 -*-
import itertools
n = int(input())
coins = []
for i in range(n):
    coins.append(int(input()))

ans = 0
patterns = list(itertools.permutations(coins))
for row in patterns:
    result = [True] * n
    for i in range(n):
        for j in range(i+1,n):
            if row[j] % row[i] == 0:
                result[j] = not result[j]
    ans += sum(result)
print(ans/len(patterns))
