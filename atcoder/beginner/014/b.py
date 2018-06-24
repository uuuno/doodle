# -*- coding:utf-8 -*-
import numpy as np
n, x = map(int, input().split())
prices = np.array(list(map(int, input().split())))
prices = prices[::-1]
bin_x = bin(x)
bin_x_list = np.array(list(bin_x.replace('0b', '').zfill(len(prices))))
bin_x_list = bin_x_list == '1'
print(sum(prices[bin_x_list]))
