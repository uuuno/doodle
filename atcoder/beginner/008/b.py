# -*- coding: utf-8 -*-
n = int(input())
votes = {}
for i in range(n):
    name = input()
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
votes_sort = sorted(votes.items(), key=lambda x: x[1])
print(list(votes_sort[-1])[0])
