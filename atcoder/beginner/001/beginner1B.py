# -*- coding:utf-8 -*-

m = int(input())
vv = ''

if m < 100:
    vv = '00'
elif m < 1000:
    vv = '0' + str(int(m/100))
elif m <= 5000:
    vv =str(int(m/100))
elif m <= 30000:
    vv = str(int((m/1000) + 50))
elif m <= 70000:
    vv = str(int((((m/1000)-30)/5)+80))
else:
    vv = '89'

print(vv)
