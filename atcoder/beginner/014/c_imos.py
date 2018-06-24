# -*- coding:utf-8 -*-
n = int(input())
result = [0] * 1000002
for i in range(n):
    a, b = map(int, input().split())
    result[a] += 1
    result[b+1] -= 1

for i in range(1, len(result)):
    result[i] += result[i-1]
print(max(result))
