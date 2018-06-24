# -*- coding:utf-8 -*-
N = input()
n_list = list(map(int, list(N)))
if int(N)%sum(n_list) == 0:
    print('Yes')
else:
    print('No')
