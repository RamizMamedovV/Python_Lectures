"""
# def create_phrase(func, word):  #это ФВП
#     func(word)

# def add_hello(s):
#     print(f"Hello {s}")

# def add_bye(s):
#     print(f"{s} bye-bye")

# create_phrase(add_hello," world")
# create_phrase(add_hello," Timur")
# create_phrase(add_bye," world")
# create_phrase(add_bye," Timur")
# 
# def calc_power(degree):
#     def calc_result(base):
#         return base ** degree
#     return calc_result

# square = calc_power(2)
# cube = calc_power(3)

# # print(calc_power(2)(4))
# print(square(8))
# print(cube(3))
# print(calc_power(2))

# calc = {"+": lambda x,y: x + y,
#         "-": lambda x,y: x - y
#         }

# print(calc["+"](8,7))
# print(calc["-"](10,7))
list_1 = ["Иванов", "Петров", "СИдоров"]
sp = [1,5,8,9,11,0,2]
# print(map(lambda x: x*2 if x>5 else 0, sp))   
# #лямбда возвращает x**2 если x> 5 иначе возвращает 0
# print(list(map(lambda x: x**2 if x>5 else 0, sp)))
# print(map(lambda x: x*2, sp))   
# print([x**2 for x in sp if x>5 ])

# print(*filter(lambda item: True if item>5 else False, sp))
# print(list(filter(lambda item: True if item>5 else False, sp)))

# for i,v in enumerate(sp):
#     print(i,v)

for s,v in zip(list_1, sp):
    print(s,v)
"""