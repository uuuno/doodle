# -*- coding:utf-8 -*
N = int(input())
nums = list(map(int, input().split()))
nums = [ nums[i]-i-1 for i in range(N) ]
nums_s = sorted(nums)
b1 = nums_s[N//2]
b2 = nums_s[N//2-1]
res = []
for b in [b1, b2]:
    result = 0
    for i in range(1,N+1):
        result += abs(nums[i-1]-b)
    res.append(result)
print(min(res))
