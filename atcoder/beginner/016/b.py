# -*- coding:utf-8 -*-
a, b, ans = map(int, input().split())
if a+b == ans or a-b == ans:
    if a+b == a-b:
        print('?')
    else:
        if a-b != ans:
            print('+')
        else:
            print('-')
else:
    print('!')
