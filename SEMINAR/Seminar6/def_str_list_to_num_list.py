def str_list_to_num_list(sorce_str_list: list) ->list:
    des_num_list = []
    j = 0
    while j < len(sorce_str_list) - 1:
        a = ''
        while sorce_str_list[j] == ' ' and j < len(sorce_str_list) - 1:
            if j < len(sorce_str_list) - 1:
                j += 1
        while sorce_str_list[j] != ' ' and j < len(sorce_str_list) - 1:
            a += sorce_str_list[j]
            if j < len(sorce_str_list) - 1:
                j += 1
        des_num_list.append(int(a))
    return des_num_list

def choose_nums(string: str):
    temp_list = string[:]
    for i in range(len(temp_list)):
        if temp_list[i] in '*-+/()':
            temp = temp_list[i]
            temp_list = temp_list.replace(temp, ' ')
    return temp_list