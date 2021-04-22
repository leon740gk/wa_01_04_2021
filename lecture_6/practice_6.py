# # map, filter, zip ================================================
# # https://dev.to/codespent/understanding-map-filter-and-zip-in-python-3ifn
# #
# # def square(number):
# #     return number * number
# # #
# # numbers = [1,2,3,4,5]
# # squared_numbers = []
# # #
# # for i in numbers:
# #     squared = square(i)
# #     squared_numbers.append(squared)
# #
# # # print(squared_numbers)
# #
# # squared_numbers = map(square, numbers)
#
# # def even(number):
# #     if (number % 2) == 0:
# #         return True
# #     else:
# #         return False
#
# # numbers = [1,2,3,4,5]
# # even_numbers = filter(even, numbers)
# #
# # even_numbers = []
# # for number in numbers:
# #     if even(number):
# #         even_numbers.append(number)
# #
# #
# def even(number):
#     if (number % 2) == 0:
#         return  True
#     return  False
# #
# # def square(number):
# #     return number*number
# #
# numbers = [1,2,3,4,5]
# even_numbers = list(filter(even, numbers))
# # even_numbers_squared = list(map(square, even_numbers))
#
#
#
# # What is lambdas ================================================
# # This is regular function
# def double(x):
#    return x * 2
#
# # The same in lambda equivalent
# double_func = lambda x: x * 2
#
# print(double(7))
# print(double_func(7))
#
#
#
# # Use lambdas ====================================================
# # Program to filter out only the even items from a list
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
#
# new_list = list(filter(lambda x: x%2 == 0, my_list))
#
# print(new_list)
#
#
# # Program to double each item in a list using map()
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
#
# new_list = list(map(lambda x: x * 2, my_list))
#
# print(new_list)
#
# # Task with lambdas ==========================================================
# # Сгенерировать пароль для пользователя.
# # Требования: длина от 6 до 20 символов, должен быть ровно один символ подчеркивания,
# # хотя бы две заглавных буквы, не более 5 цифр, любые две цифры подряд недопустимы.
#
# # import random
# #
# # def pass_generator():
# #     lower_letters = lambda: chr(random.randint(97, 122))
# #     upper_letters = lambda: chr(random.randint(65, 90))
# #     numbers = lambda: chr(random.randint(48, 57))
# #     underscore = lambda: chr(95)
# #     list_of_values = [lower_letters, upper_letters, numbers, underscore]
# #     choose_flow = [3, 1, 0, 0, 0, 2, 1, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 1, 2]
# #
# #     password = ""
# #     for i in range(random.randint(6, 20)):
# #         symbol = list_of_values[choose_flow[i]]
# #         password += symbol()
# #
# #     return password
#
#
#
# # About sorted() ================================================
# sorted(iterable, key=None, reverse=False)
# vowels list
# py_list = ['e', 'a', 'u', 'o', 'i']
# print(sorted(py_list))

# # string
# py_string = 'Python'
# print(sorted(py_string))
#
# # vowels tuple
# py_tuple = ('e', 'a', 'u', 'o', 'i')
# print(sorted(py_tuple))
#
# # sorted(iterable, key=len) ------------------------------------------
# test_iterable = ["123", "24455", "23455", "67856785", "9485", "3"]
# a_list = [(1, 2), (3, 5), (4, 1), (2, 5)]
# print(sorted(a_list))
#
# def sorter(a_tuple):
#     return (a_tuple[1], a_tuple[0])
#
# print(sorted(a_list, key=sorter))
# print(sorted(test_iterable, key=len, reverse=True))
# # sorted(test_iterable, key=len)
# def sorter(item):
#     res = [len(item), item[0]]
#     # if len(item) > 1:
#     #     res.append(item[1])
#     return res

# # sorted(iterable, key=custom_func) ------------------------------------------
# # take the second element for sort
# def take_second(elem):
#     return elem[1], elem[0]
#
# random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3), (5, 2)]
# sorted(random)

# sort list with key
# sorted_list = sorted(random, key=take_second)
# print(sorted(random, key=lambda x: (x[1], x[0])))
#
# # print list
# print('Sorted list:', random)
# # ----------------------------------------------------------------------------
# # Nested list of student's info in a Science Olympiad
# # List elements: (Student's Name, Marks out of 100 , Age)
# participant_list = [
#     ('Alison', 50, 18),
#     ('Terence', 75, 12),
#     ('David', 75, 20),
#     ('Jimmy', 90, 22),
#     ('John', 45, 12)
# ]
#
#
# def sorter(item):
#     return ((100 - item[1]), item[2])
#
#
# a = lambda item: (100-item[1], item[2])

#
# sorted_list = sorted(participant_list, key=sorter)
# print(sorted_list)
#
# # The same but with lambda ---------------------------------------------------
# # Nested list of student's info in a Science Olympiad
# # List elements: (Student's Name, Marks out of 100 , Age)
# participant_list = [
#     ('Alison', 50, 18),
#     ('Terence', 75, 12),
#     ('David', 75, 20),
#     ('Jimmy', 90, 22),
#     ('John', 45, 12)
# ]
#
# sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
# print(sorted_list)
#
#
# # Tim Sort ! -----------------------------------------------------------------
# # https://www.geeksforgeeks.org/timsort/
#
#
# # Decorators =================================================================
# # https://gist.github.com/Zearin/2f40b7b9cfc51132851a
#
#
#
#
# # Functools ==================================================================
# # https://www.geeksforgeeks.org/functools-module-in-python/
# # partial --------------------------------------------------------------------
# from functools import partial
#
# def power(a, b):
#     return a ** b
#
# # partial functions
# pow2 = partial(power, b = 2)
# pow4 = partial(power, b = 4)
# power_of_5 = partial(power, 5)
#
# print(power(2, 3))
# print(pow2(4))
# print(pow4(3))
# print(power_of_5(2))
#
# print('Function used in partial function pow2 :', pow2.func)
# print('Default keywords for pow2 :', pow2.keywords)
# print('Default arguments for power_of_5 :', power_of_5.args)
#
#
# # cmp_to_key -----------------------------------------------------------------
# from functools import cmp_to_key
#
# # function to sort according to last character
# def cmp_fun(a, b):
#     if a[-1] > b[-1]:
#         return 1
#     elif a[-1] < b[-1]:
#         return -1
#     else:
#         return 0
#
# list1 = ['geeks', 'for', 'geeks']
# l = sorted(list1, key = cmp_to_key(cmp_fun))
# print('sorted list :', l)
#
# # lru_cache ------------------------------------------------------------------
# from functools import lru_cache
#
# @lru_cache(maxsize = None)
# def factorial(n):
#     if n<= 1:
#         return 1
#     return n * factorial(n-1)
# print([factorial(n) for n in range(7)])
# print(factorial.cache_info())
#
# # singledispatch  ------------------------------------------------------------
# from functools import singledispatch
#
# @singledispatch
# def fun(s):
#     print(s)
# @fun.register(int)
# def _(s):
#     print(s * 2)
#
# fun('GeeksforGeeks')
# fun(10)
#
#
# # Tasks to solve =============================================================
#
# # https://py.checkio.org/en/mission/morse-decoder/
# # to solve
#
# # https://py.checkio.org/en/mission/split-list/
# # To solve
#
# # https://py.checkio.org/ru/mission/date-and-time-converter/
# # To solve