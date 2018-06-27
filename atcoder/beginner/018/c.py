# -*- coding:utf-8 -*-
R, C, K = map(int, input().split())
matrix = []
for i in range(R):
    matrix.append(list(input()))

g_size = 0
for i in range(1, 2*K, 2):
    g_size += i
g_size = (g_size*2) - (2*K-1)

count = 0
for x in range(K-1, R-K+1):
    for y in range(K-1, C-K+1):
        g_count = 0
        for i in range(x-K+1,x+K): #x方向に取りうるi
            for j in range(y-K+1+abs(i-x), y+K-abs(i-x)): #y方向で取りうるj
                if matrix[i][j] == 'o':
                    g_count += 1
                else:
                    break
        if g_count == g_size:
            count += 1
print(count)
