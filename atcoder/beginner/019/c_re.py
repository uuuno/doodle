# -*- coding:utf-8 -*
N = int(input())
nums = list(map(int, input().split()))
for i in range(N):
    while nums[i]%2==0:
        nums[i]//=2
nums=set(nums)
print(len(nums))
