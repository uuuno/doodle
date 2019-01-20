# -*- coding:utf-8 -*
s = int(input())
n_list = []
n_list.append(s)
end_flag = False
while not end_flag:
    if n_list[-1]%2 == 0:
        if (n_list[-1]/2) in n_list:
            print(len(n_list)+1)
            end_flag = True
        else:
            n_list.append(n_list[-1]/2)
    else:
        if (3*(n_list[-1])+1) in n_list:
            print(len(n_list)+1)
            end_flag = True
        else:
            n_list.append(3*(n_list[-1])+1) 
