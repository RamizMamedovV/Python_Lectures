from def_str_list_to_num_list import *

# def result(num1, num2, index):
#     if index == '*':
#         return num1 * num2
    

# # list1 = '1*12*(40+60)'
# list1 = '1*12'
p = '*'
d = '/'
s = '+'
m = '-'
# left = []
# right = []

# if p in list1:
#     left.append(list1[0: list1.index(p)])
#     right.append(list1[list1.index(p)+ 1:])
#     print(result(int(left), int(right), p))

# user_input = '-1*12*(40+(2 * (2* 15)))*(2+ 4)'
user_input = '(-1+12)*(40+(2 * (2* 15)))*(2+ 4)'

list_str_nums = choose_nums(user_input)

nums_int_list = str_list_to_num_list(list_str_nums) # [1, 12, 40, 2, 2, 15, 2, 4]

# print(list_str_nums)
# print(nums_int_list)

def priority_exercises():
    prior = []
    priors = {}
    count = 0
    inp = '(-1+12)*(40+(2 * (2* 15)))*(2+ 4)'
    i = 0
    while i < len(inp):
        if inp[i] == '(':
            i += 1
            if inp[i] != ')':
                while inp[i] != ')':
                    if inp[i] == '(':
                        prior = prior.clear
                        prior = []
                        i += 1
                        continue
                    else:    
                        prior.append(inp[i])
                        i += 1
            priors[count] = prior
            count += 1
            prior = prior.clear
            prior = []
        else:
            i += 1    

    print(priors)

priority_exercises()
# print(pr)
