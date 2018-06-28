# -*- coding:utf-8 -*
N = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

count = 0
while len(nums) > 0:
    j = 0
    base = nums[0]
    count += 1
    while base*(2**j) <= max(nums):
        if base*(2**j) in nums:
            nums.remove(base*(2**j))
        j += 1
        if len(nums) == 0:
            break
print(count)
