# -*- coding: utf-8 -*-
import math
tx_s, ty_s, tx_g, ty_g, T, V = list(map(int, input().split()))
n = int(input())
girls = []
for i in range(n):
    girls.append(list(map(int, input().split())))

possibility = False;
for cood in girls:
    distance = math.sqrt((cood[0]-tx_s)**2 + (cood[1]-ty_s)**2)
    distance += math.sqrt((cood[0]-tx_g)**2 + (cood[1]-ty_g)**2)
    if distance <= T*V:
        possibility = True
        break;

if possibility:
    print('YES')
else:
    print('NO')
