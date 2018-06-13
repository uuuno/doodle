# -*- coding:utf-8 -*-
pre = list(map(int, input().split()))
n = pre[0]
k = pre[1]
rates = list(map(int, input().split()))
rates.sort()
my_rate = 0
for i in range(k):
    my_rate = (my_rate+rates[n-k+i])/2
print(my_rate)
