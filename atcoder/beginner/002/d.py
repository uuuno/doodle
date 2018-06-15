# -*- coding:utf-8 -*-
n, m = map(int, input().split())
relations = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    relations[x-1][y-1] = 1
    relations[y-1][x-1] = 1
    relations[x-1][x-1] = 1
    relations[y-1][y-1] = 1
print(relations)

result = 1

for i in range(2**n):
    people = []
    for j in reversed(range(1,n+1)):
        if i&(1<<j-1):
            people.append(j)
    print(people)
    flag = 0
    for person_a in people:
        for person_b in people:
            if relations[person_a-1][person_b-1] != 1 :
                flag = -1
    if flag == 0:
        result = max(result,len(people))
print(result)
