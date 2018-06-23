# -*- coding:utf-8 -*-
n = int(input())
ng = []
for i in range(3):
    ng.append(int(input()))

if n in ng:
    print('NO')
    exit()

count = 0
while n!=0:
    if count == 100:
        print('NO')
        exit()

    fail = True
    for i in [3,2,1]:
        if n-i >= 0 and (not n-i in ng):
            n -= i
            count += 1
            fail = False
            break

    if fail:
        print('NO')
        exit()
    elif n == 0:
        print('YES')
