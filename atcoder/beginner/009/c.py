# -*- coding: utf-8 -*-
import numpy as np
n, k = list(map(int, input().split()))
s = list(input())
t = sorted(s)
now = []
rest = sorted(s[:])

def judge(now, candi, rest):
    diff = 0
    now += candi
    rest.remove(candi)

    # 決定している箇所のミスマッチ数
    for i in range(len(now)):
        if now[i] != s[i]:
            diff += 1

    # 残り箇所の最小ミスマッチ数
    if len(rest) > 0:
        mismatch = s[-len(rest):]
    else:
        mismatch = []
    for i in rest:
        if i in mismatch:
            mismatch.remove(i)

    if diff + len(mismatch) <= k:
        return True
    else:
        return False

for _ in range(n):
    for candi in rest:
        if judge(now[:], candi, rest[:]):
            now += candi
            rest.remove(candi)
            break

print(''.join(now))
