# -*- coding:utf-8 -*-
n = int(input())
h = int(n/3600)
n = n%3600
m = int(n/60)
n = n%60
print(str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(n).zfill(2))
