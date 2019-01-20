# -*- coding:utf-8 -*
N = int(input())
h_list = list(map(int, input().split()))
pour_cnt = 0

def cnt(remains, pour_cnt):
    tmp = []
    next_remains = []
    # print(remains)
    for index, num in enumerate(remains):
        if num != 0:
            tmp.append(num)
            if (index+1 == N):
                min_num = min(tmp)
                pour_cnt += min_num
                for tmp_num in tmp:
                    next_remains.append(tmp_num-min_num)
                tmp = []
        elif len(tmp) != 0:
            min_num = min(tmp)
            pour_cnt += min_num
            for tmp_num in tmp:
                next_remains.append(tmp_num-min_num)
            next_remains.append(0)
            # print(tmp)
            tmp = []
        else:
            next_remains.append(0)

    if next_remains.count(0) == N:
        print(pour_cnt)
    else:
        cnt(next_remains, pour_cnt)

cnt(h_list, pour_cnt)