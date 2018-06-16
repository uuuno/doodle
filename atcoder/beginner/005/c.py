# -*- coding:utf-8 -*-
t = int(input())
n = int(input())
tkyk = list(map(int, input().split()))
m = int(input())
cus = list(map(int, input().split()))
if m > n:
    print('no')
else:
    start = 0
    for i in range(m):
        for j in range(start, n):
            if tkyk[j] <= cus[0] and tkyk[j]+t >= cus[0]:
                del cus[0]
                start = j+1
                break
    if len(cus) == 0:
        print('yes')
    else:
        print('no')
