# -*- coding: utf-8 -*-
n = int(input())
prices = set([])
for i in range(n):
    prices.add(int(input()))
print(sorted(prices, reverse=True)[1])
