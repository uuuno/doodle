# -*- coding:utf-8 -*-

input_data = input().split()
deg = int(input_data[0])
wind = int(input_data[1])

degs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
deg_min = [
112.5,
337.5,
562.5,
787.5,
1012.5,
1237.5,
1462.5,
1687.5,
1912.5,
2137.5,
2362.5,
2587.5,
2812.5,
3037.5,
3262.5
]

DEG = ''
count = 0
if deg < 112.5 or deg >3487.5:
    DEG = N
else:
    for i in deg_min:
        if deg >= i:
            count += 1

print(degs[count])
