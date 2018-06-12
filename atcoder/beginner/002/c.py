# -*- coding:utf-8 -*-
coor = list(map(int, input().split()))
x_std, y_std = coor[0], coor[1]
area = abs((coor[2]-x_std)*(coor[5]-y_std)-(coor[3]-y_std)*(coor[4]-x_std))/2
print(area)
