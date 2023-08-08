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

list1 = '-1*12*(40+60)*(2+ 4)'
list2 = list1[:]

for i in range(len(list2)):
    if list2[i] in '*-+/()':
        temp = list2[i]
        # print(temp)
        list2 = list2.replace(temp, ' ')
        
print(list2)
list3 = list2.split()
list3.append(list2)
print(list3)
