# -*- coding:utf-8 -*-
n = int(input())
nums = list(range(1,7))
n = n % 30
for i in range(n):
    l_index = (i%5)
    r_index = (i%5)+1
    nums[r_index], nums[l_index] = nums[l_index], nums[r_index]
print(''.join(map(str, nums)))
