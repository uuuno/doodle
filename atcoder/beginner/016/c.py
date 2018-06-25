# -*- coding:utf-8 -*-
n, m = map(int, input().split())
friends = { i:[] for i in range(1,n+1) }
result = { i:set([]) for i in range(1,n+1) }
for i in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for key, value in friends.items():
    for val in value:
        for v in friends[val]:
            if v != key and (not v in value):
                result[key].add(v)
    print(len(result[key]))
