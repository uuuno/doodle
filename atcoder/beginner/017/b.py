# -*- coding:utf-8 -*-
word = input()
if word == '':
    print('YES')
else:
    w = word.replace('ch', '')
    if len(w) == w.count('o') + w.count('k') + w.count('u'):
        print('YES')
    else:
        print('NO')
