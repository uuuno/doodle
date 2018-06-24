# -*- coding: utf-8 -*-
n, k = map(int, input().split())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
res = 'Nothing'

def check(dep, val):
    if dep == n:
        return (val == 0)
    for i in range(k):
        if check(dep+1, val^nums[dep][i]):
            return True
    else:
        return False

if check(0,0):
    print('Found')
else:
    print('Nothing')
