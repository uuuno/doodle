# -*- coding:utf-8 -*-
ws = input()
now = ''
count = 0
result = []
for i, s  in enumerate(ws):
    if now != s:
        if i != 0:
            result.append(str(count))
        result.append(s)
        count = 1
        now = s
    else:
        count += 1
    if i == len(ws)-1:
        result.append(str(count))
print(''.join(result))
