# -*- coding:utf-8 -*-
s = list(input())
s[0] = s[0].upper()
for i, str in enumerate(s[1:]):
    s[i+1] = str.lower()
print(''.join(s))
