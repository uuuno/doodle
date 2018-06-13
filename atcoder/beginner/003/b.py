# -*- coding:utf-8 -*-
str1 = input()
str2 = input()
flag = True
wild_char = ['a', 't', 'c', 'o', 'd', 'e', 'r', '@']
for i in range(len(str1)):
    if str1[i] != str2[i]:
        if str1[i] != '@' and str2[i] != '@':
            flag = False
        else:
            if (not str1[i] in wild_char) or (not str2[i] in wild_char):
                flag = False

if flag:
    print('You can win')
else:
    print('You will lose')
