                                            # List Списки
# list_1 = []
# list_2 = list()
# print(list_1, list_2)        # [] []
# list_1 = [1, 2, 3, 4]
# print(*list_1)              # 1 2 3 4 (*) - without []  
      
# for i in list_1:
#    print(i)                # 1 2 3 4
#    print(len(list_1))

# for i,v in enumerate(list_1):           # распечатает ключ и значение
#     print(i, v)

# to add and del elem
# list = [1, 2]
# list.append(8)              # added element in the end of the list [1, 2, 8]
# list.extend([5,7])          # extends with the new list [1, 2, 8, 5, 7] вместо append
# print(list)
# print(list.pop())           # delete and return the last elem (if did not specified) 
#                                                                # pop(2) - second elem
# print(list)
# list.insert(2, 88)             # add an elem (88) to the 2 posicion 
# print(list)
# print(list[-1])                 # print the last elem
# print(list[:2])                 # 1 2
# print(list[::2])                 # 1 88




                            # TUPLE   КОРТЕЖ - неизменяемый список

# t = ()                              # created type <class 'tuple'>
# t1 = (1,)                           # <class 'tuple'>
# print(type(t1))
# tu = [1, 2, 3]                        # <class 'int'>
# t2 = tuple(tu)                        # <class 'tuple'>
# print(tu, t2)                          # [1, 2, 3] (1, 2, 3)
# a, b, c = t2
# print(a, b, c)                         # a = 1, b = 2, c = 3/ print 1 2 3
# a = b = c = t2[0]                      # a = 1, b = 1, c = 1/ print 1 1 1
# for i in t2:
#     print(i)                            # 1 2 3
# for i in range(len(t2)):
#     print(t2[i])                            # 1 2 3




                        # DICTIONARY  СЛОВАРИ - неупорядоченные, с доступом по ключу
# d = {}                              # <class 'dict'>
# d1 = dict()                         # <class 'dict'>
# d['clue'] = 'CLUE'
# d1['key'] = 'key1'
# print(d, d1)                     # {'clue': 'CLUE'} {'key': 'key1'}
# d1['keyDict'] = d                # {'key': 'key1', 'keyDict': {'clue': 'CLUE'}} словарь в словаре
"""
for i in d1:                            # key: key1
    print('{}: {}'.format(i, d1[i]))    # keyDict: {'clue': 'CLUE'}
"""

"""
for (k, v) in d1.items():              # key: key1
    print(k, v)                        # keyDict: {'clue': 'CLUE'}
"""

"""
print(d1.items())                   # dict_items([('key', 'key1'), ('keyDict', {'clue': 'CLUE'})])
"""                                 #  список кортежей tuple

# del d1['keyDict']                  # delete d1['keyDict']
# print(d1)




                                # SET МНОЖЕСТВА - уникалные элем-ты, 
# не упорядоченные. содержат любые типы. 
# возможно 2 множества операции: обединять, пересечение, разность!

# s = set()                                   # create a set()
# colors = {'red', 'green', 'blue'}         #  # type: <class 'set'>
# colors.add('red')                           # {'red', 'green', 'blue'}  DO NOT ADD
# colors.add('grey')                          # {'red', 'blue', 'grey', 'green'} ADDED
# print(red in colors)                        # True если содержит
# colors.remove('red')                        # removed
# colors.remove('red')                        # KeyError если нет элкмкнта, ВЫДАСТ ОШИБКУ
# colors.discard('red')                        # УДАЛИТ, НО если нет элкмкнта, то не выдаст ошибку
# colors.clear()                             # cleared and print: set()
# print(colors)

# операции: обединять, пересечение, разность!
# a = {1, 2, 3, 4, 5, 8}
# b = {1, 8, 5, 7, 9, 0}
# c = a.copy()                        # c = {1, 2, 3, 4, 5,8}
# u = a.union(b)                       # u = {0, 1, 2, 3, 4, 5, 7, 8, 9}
# i = a.intersection(b)               # {8, 1, 5}
# d1 = a.difference(b)                                 # {2, 3, 4}
# d2 = b.difference(a)                                 # {0, 9, 7}
# uni = a.union(b).difference(a.intersection(b))      # {0, 2, 3, 4, 7, 9} 
#                                                 # u = {0, 1, 2, 3, 4, 5, 7, 8, 9} diff i = {8, 1, 5}
# x, y, z = i
# print(x, y, z)



#                                   FROZENSET ЗАМОРОЖЕННОЕ МНОЖЕСТВО

# a = {1, 2, 3}
# f = frozenset(a)                        # frozenset({1, 2, 3})
# print(f)



                            # LIST COMPREHENSION ГЕНЕРАТОР СПИСКОВ - упрощен. 
                            # подход к созданию списков исп-уя for, if-else
# list = [i for i in range(1, 100)]           # [1, 2, .....98, 99]
# list = [i for i in range(1, 100) if i % 2 == 0]           # [2, 4, .....98]
# list = [(i, i) for i in range(1, 100) if i % 2 == 0]           # [(2, 2), (4, 4), .....(98, 98)] tuples
# list = [i * i for i in range(1, 10) if i % 2 == 0]           # [4, 16, 36, 64] 
# print(list)