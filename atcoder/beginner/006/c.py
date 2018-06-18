# -*- coding: utf-8 -*-
n, m = map(int, input().split())
if m%2==0:
    older = 0
    for i in range(n+1):
        if (2*i+4*(n-i)) == m:
            print(i,older,n-i)
            exit()
else:
    older = 1
    m -= 3
    n -= 1
    for i in range(n+1):
        if (2*i+4*(n-i)) == m:
            print(i,older,n-i)
            exit()
print(-1,-1,-1)
