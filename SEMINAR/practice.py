

exercise = '3+2*4*(5+65)'
p = '*'
d = '/'
s = '+'
m = '-'
br_l = '('
br_r = ')'
priority1 = ''
delet = ''
res = ''
if br_l in exercise:
    delet = exercise[exercise.index(br_l):exercise.index(br_r) + 1]
    for i in exercise[exercise.index(br_l) + 1:exercise.index(br_r)].split():
        priority1 += i
    if s in priority1:
        res = int(priority1[0]) + int(priority1[2:])
        print(res)
exercise = exercise.replace(str(delet), str(res))
if p in exercise:
    delet = exercise[exercise.index(p)-1 : exercise.index(p) + 2]
    print(type(delet))
    if p in delet:
        res = int(delet[0]) * int(delet[2])
        print(res)
exercise = exercise.replace(str(delet), str(res))
if p in exercise:
    delet = exercise[exercise.index(p)-1 : exercise.index(p) + 2]
    print(type(delet))
    if p in delet:
        res = int(delet[0]) * int(delet[2])
        print(res)
exercise = exercise.replace(str(delet), str(res))
if s in exercise:
    delet = exercise[exercise.index(s)-1 : exercise.index(s) + 2]
    print(type(delet))
    if s in delet:
        res = int(delet[0]) + int(delet[2])
        print(res)
exercise = exercise.replace(str(delet), str(res))
print(exercise)


# print(exercise)










# p = '*'
# a = exercise.index(p)
# b = int(exercise.index(p)) - 1
# c = int(exercise.index(p)) + 1
# print(a)
# print(b)
# print(c)
# print(int(exercise[b]) * int(exercise[c]))
# tree = {}
# print(exercise.index(p))
# exercise.pop(exercise.index(p))
#print(int(exercise.pop(exercise.index(p))) * int(exercise.pop(exercise.index(p)-1)))
# print(prior(tree, exercise))










# def prior(tree: dict, string: str,string_right = '', count = 1):
#     if len(string) == 0:
#         return tree
#     p = '*'
#     s = '+'
#     if p in string:
#         string_right = string[string.index(p)+1:]
#         string = string[0:string.index(p)]
#         tree[count] = p
#         count *= 2
#         print(string)
#         print(string_right)
#         return prior(tree, string, string_right, count)
#     elif s in string:
#         string_right = string[string.index(s) + 1:]
#         string = string[0:string.index(s)]
#         tree[count] = s
#         count *= 2
#         print(string)
#         print(string_right)
#         return prior(tree, string, string_right, count)
#     print(string)
#     print(string_right)
#     # left = list(left.split())
#     # right = list(right.split())
#     tree[count] = string
#     count *= count
#     count += 1
#     tree[count] = string_right
#     return tree


# exercise = '3 + 2 * 4'
# tree = {}
# print(prior(tree, exercise))
# # print(exercise.index(p))


# def prior(tree: dict, string: list, count = 1):
#     res = 0
#     if len(string) == 0:
#         return tree
#     p = '*'
#     s = '+'
#     if p in string:
#         string.pop(string.index(p))
#         res = int(string.pop(string.index(p)-1)) * int(string.pop(string.index(p)-1))
#         count *= 2
#         print(string)
#         return prior(tree, string, count)
#     elif s in string:
#         string = string[0:string.index(s)] + ' ' + string[string.index(s)+1:]
#         tree[count] = s
#         count += 1
#         print(string)
#         return prior(tree, string, count)
#     else:
#         print(string)
#         string = enumerate(string)

#     return tree
