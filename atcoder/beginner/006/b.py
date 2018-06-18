# -*- coding:utf-8 -*-
n = int(input())
nums = [0, 0, 1]
if n <= 3:
    print(nums[n-1])
else:
    for i in range(3, n):
        nums.append((nums[i-1]+nums[i-2]+nums[i-3])%10007)
    print(nums[-1])
