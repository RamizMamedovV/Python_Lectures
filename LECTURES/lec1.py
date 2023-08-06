# print("ctrl + f5")                #для запуска последней кода python
# print("<-")
# print("python lec1.py")                 #для запуска кода python
# print(5, 6, 5) # 5 6 5
"""  закоментить кусок кода
# # ctrl + k ; ctrl + c # закоментить
# # ctrl + k ; ctrl + u # раскоментить
"""

# n = 5 # 5
# n = None # None
# n = 1.89 # 1.89
# n = 'te\'xt' # te'xt
# m = 'te"text"xt' # te"text"xt
# print(n, m)
# print(type(n)) # <class 'str'>

# a = 0
# b = 1.11
# c = 'text'
# print(a, '- ',b, '- ', c) # 0 -  1.11 -  text
# print(f"{a} - {b} - {c}") # 0 -  1.11 -  text
# print("{} - {} - {}".format(a,b,c)) # 0 -  1.11 -  text


# a = input("Enter your first1 number: ") # 2
# b = input("Enter your second number: ") # 3
# print(a + b)                            # 23 (becouse the a and b are strings!!)

# a = 7.2
# print(type(a)) # <class float>
# i = int(a)
# print(i) # 7 int
# s = str(a)
# print(s + ' text') # 7.2 text str
# b = bool(a)
# print(b) # True

# a = int(input("Enter your first1 number: "))# 2
# b = float(input("Enter your second number: ")) # 3.9876
# print(a + b)                            # 5.9876000000005 (becouse the b is float!!)
# print(round(a * b, 4))                            # 7.9752 (becouse the b is float!!)
# print(a ** 5)                                   # 2^5 = 32

# a = 1 > 5
# print(a)            # False
# a = 1 < 4 and 5 > 2 # true
# print(a)
# a = 1 == 2
# print(a)            # False
# a = 'aaz'
# b = 'aaz'
# print(a == b)       # True
# a = 1 < 2 < 5 > 2   # True because 1 < 2 ; 2 < 5 ; 5 > 2
# print(a)

# i = 0
# while i < 5:
#     if i == 3:
#         break     # 3 because break но лучше применять flag
#     i += 1
# else:
#     print('text')
# print(i)

# i = 2
# flaq = True
# n = 25
# while flaq:
#     if n % i == 0:
#         flaq = False
#         print(i)
#     else:
#         flaq = False
#         print('text')
# print(i)

# for i in 1, 2, 5:
#     print(i)              # 1 2 5
# for i in range(5):
#     print(i)                # 0 1 2 3 4
# for i in range(1, 10, 2):
#     print(i)                   # 1 3 5 7 9
# for i in range(10, 0, -2):
#     print(i)                   # 10 8 6 4 2

# text = 'abcDE'
# print(text[2])                     # c
# for i in text:
#    print(i)                   # a b c D E
# print('ab' in  text)           # True
# print(text.lower())             # abcde
# print(text.upper())                     #ABCDE
# print(text.replace('ab', 'HELLO'))      #HELLOcDE

# text = 'abcdef ghijklmnop qrstuv wxyz'
# print(text[len(text)-1])                        # z
# print(text[:])                                  # abcdef ghijklmnop qrstuv wxyz
# print(text[:2])                                 # ab
# print(text[2:5])                                # cde
# print(text[7:-15])                              # ghijklm
# print(text[0 : len(text) : 5])                  # afjosw    step = 5
# print(text[ : : 5])                               # afjosw    step = 5
# text = text[2:9] + ' ' + text [2:9]
# print(text)                                       # cdef gh cdef gh