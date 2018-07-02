# -*- coding:utf-8 -*-
H, W, T = map(int, input().split())
maps = []
s_cood = []
g_cood = []
for i in range(H):
    tmp = list(input())
    maps.append(tmp)
    if 'S' in tmp:
        s_cood.append(i)
        s_cood.append(tmp.index('S'))
    if 'G' in tmp:
        g_cood.append(i)
        g_cood.append(tmp.index('G'))
