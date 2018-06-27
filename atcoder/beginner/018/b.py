# -*- coding:utf-8 -*-
s = list(input())
n = int(input())

for _ in range(n):
    l,r = map(int, input().split())
    target = s[l-1:r]
    target.reverse()
    s = s[:l-1] + target + s[r:]
print(''.join(s))
