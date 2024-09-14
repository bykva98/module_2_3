my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
begin = 0
while begin < len(my_list):
    if my_list[begin] > 0:
        print(my_list[begin])
    elif my_list[begin] == 0:
        pass
    else:
        break
    begin = begin+1
    continue


