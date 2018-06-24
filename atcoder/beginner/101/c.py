# -*- coding:utf-8 -*-
import math
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
one_index = nums.index(1)
if k == len(nums):
    print(1)
else:
    print(math.ceil((n-1)/(k-1)))
