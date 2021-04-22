# Dictionaries ---------------------------------------------------------------------------
# Пользователь вводит номер месяца, вывести название месяца.
# month_mapper = {
#     "1": "January",
#     "2": "Feb",
#     "3": "March",
# }
#
# while True:
#     user_input = input("PLease enter month number (1-12), for exit please enter 0: ")
#     if user_input == "0":
#         break
#     print(month_mapper.get(user_input, "Please enter valid number (1-12)"))


# ====================================================================================
# A bit more about dictionaries ------------------------------------------------------
# keys, values, items(), iteration ---------------------------------------------------
# employee = {
#   "name": "John Doe",
#   "age": 27,
#   "nationality": "Japanese"
# }
# employee_2 = {
#   "name": "John Doe_2",
#   "age": 24,
#   "nationality": "Ukrainian"
# }
# employee_3 = {
#   "name": "John Doe_3",
#   "age": 29,
#   "nationality": "Italian"
# }
# employee_list = [employee, employee_2, employee_3]
#
# for k, v in employee_3.items():
#     print(f"{k} --> {v}")






# ====================================================================================
# DRY --------------------------------------------------------------------------------
# So, why functions? -----------------------------------------------------------------
# O(N**2) ----------------- Insertion Sort -------------------------------------------
# https://www.geeksforgeeks.org/insertion-sort/ --------------------------------------
# a_list = [1, 334, 546, 234, 76, 3445, 4, 45, 3, 234, 4, 2334]
# a_list_2 = [1, 334, 546, 234, 76, 345, 4, 45, 3, 453, 4, 2334]
# a_list_3 = [1, 334, 546, 2345, 76, 3445, 4, 45, 3, 234, 4, 2334]
# a_list_4 = [1, 334, 546, 234, 76, 3445, 4, 445, 3, 234, 4, 2334]
#
# len_array = len(a_list)
# for i in range(1, len_array):
#     key = i
#     while key > 0 and a_list[key - 1] > a_list[key]:
#         a_list[key - 1], a_list[key] = a_list[key], a_list[key - 1]
#         key -= 1
#
# print(a_list)

# a = 4
# b = 5
# c = 7
#
# def sum_all(num):
#     num += 1
#
#     return num
#
# result_1 = sum_all(a)
# result_2 = sum_all(b)
# result_3 = sum_all(c)
#
# print(result_1)
# print(result_2)
# print(result_3)
#
# print(a)
# print(b)
# print(c)


# a_list = [1, 334, 546, 234, 76, 3445, 4, 45, 3, 234, 4, 2334]
# a_list_2 = [1, 334, 546, 234, 76, 345, 4, 45, 3, 453, 4, 2334]
# a_list_3 = [1, 334, 546, 2345, 76, 3445, 4, 45, 3, 234, 4, 2334]
# a_list_4 = [1, 334, 546, 234, 76, 3445, 4, 445, 3, 234, 4, 2334]
#
# def insertion_sort(a_list):
#     len_array = len(a_list)
#     for i in range(1, len_array):
#         key = i
#         while key > 0 and a_list[key - 1] > a_list[key]:
#             a_list[key - 1], a_list[key] = a_list[key], a_list[key - 1]
#             key -= 1
#
# insertion_sort(a_list)
# insertion_sort(a_list_2)
# insertion_sort(a_list_3)
# insertion_sort(a_list_4)
#
# print(a_list)
# print(a_list_2)
# print(a_list_3)
# print(a_list_4)

# Implementations here ---------------------------------------------------------------


# def adder(a: int, b: int, c: int, d: int=4, e: int=57) -> int:
#     if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
#         return "Not valid date was input"
#     result = a + b + c + d + e
#     return result
#
#
# if __name__ == "__main__":
#     adder("ddd", "fdgff", "Sffsfgsfgg")


# ====================================================================================
# Function args ----------------------------------------------------------------------
# from typing import Callable
#
#
# def upper_case(input_string: str) -> str:
#     string_1 = input_string.upper()
#     return string_1
#
# def lower_case(input_string: str) -> str:
#     string_2 = input_string.lower()
#     return string_2
#
# def string_changer(input_func: Callable, input_string: str) -> str:
#     result = input_func(input_string)
#     return result
#
#
# if __name__ == "__main__":
#     test_string = "How much is this fish ? ))"
#     result_1 = string_changer(upper_case, test_string)
#     result_2 = string_changer(lower_case, test_string)
#     print(result_1)
#     print(result_2)



# ====================================================================================
# Local Scope ------------------------------------------------------------------------
# a = 78
#
# def foo(c):
#     c + a
#     print(a)
#
# foo(5)
# print(c)


# a = 7
# print(a)
#
# def foo():
#     global a
#     a = a + 1
#     print(a)
#
# foo()
# print(a)

# Enclosing Scope (Nonlocal Scope) ---------------------------------------------------
# a = 7
#
# def red():
#     b = 8
#     def blue():
#         global a
#         nonlocal b
#         b += 1
#         print(a)
#         print(b)
#     blue()
#     print(a)
#
# red()

# a = []
# for i in range(40):
#     a.append(i)


# Built-in Scope ---------------------------------------------------------------------

# def len(container):
#     result = []
#     for i in container:
#         result.append(i ** 2)
#
#     return result
#
# print(len([1,2,3,4]))

# def my_len(input_string):
#     return input_string + "this is my global function"
#
# print(len("12345"))

# Never give a names for you vars, funcs, class the same as Python reserved
# https://www.tutorialspoint.com/What-are-Reserved-Keywords-in-Python




# Closures ---------------------------------------------------------------------------
# http://www.trytoprogram.com/python-programming/python-closures/
# https://www.programiz.com/python-programming/closure


# def func1():  #Outer function
#   msg = 'I belong to func1'
#   def func2(): #Nested function
#       print (msg)
#   return func2
#
# result = func1()


# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
#
#
# # Multiplier of 3
# times3 = make_multiplier_of(3)
#
# # Multiplier of 5
# times5 = make_multiplier_of(5)
#
# # Output: 27
# print(times3(9))
#
# # Output: 15
# print(times5(3))
#
# # Output: 30
# # print(times5(times3(2)))
# def my_max():
#     result = max(sdfvldns)
#     dkvhdsfkv
#     sdfvdfv
#
# max()


# ====================================================================================
# Recursion and call stack -----------------------------------------------------------
# https://realpython.com/python-thinking-recursively/



# def factorial_recursive(n):
#     return 1 if n == 1 else n * factorial_recursive(n-1)
#
#
# if __name__ == "__main__":
#     result = factorial_recursive(7)
#     print(result)


# factorial without recursion
# n = int(input("Enter the number: "))
# fact = 1
# if n < 0:
#     print("factorial doesn't exist for negative numbers")
# else:
#     for i in range(1, n+1):
#         fact = fact * i
#     print("factorial of", n, "is", fact)

# def sum_recursive(current_number, accumulated_sum, number_till):
#
#     if current_number == number_till:
#         return accumulated_sum
#
#     else:
#         return sum_recursive(current_number + 1, accumulated_sum + current_number, number_till)
#
# if __name__ == '__main__':
#     sum_recursive(1, 0, 11)


# Tasks to solve ---------------------------------------------------------------------

# https://py.checkio.org/en/mission/morse-decoder/
# to solve
MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(input_data):
    words = input_data.split("   ")
    output_list = []
    for word in words:
        letters = word.split()
        phrase = ""
        for i in letters:
            phrase += MORSE[i]
        output_list.append(phrase)

    if output_list[0][0].isalpha():
        output_list[0] = output_list[0].capitalize()

    result = " ".join(output_list)

    return result

if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")

# https://py.checkio.org/en/mission/split-list/
# To solve

# https://py.checkio.org/ru/mission/date-and-time-converter/
# To solve