# Basic operations -----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит два числа. Найдите сумму и произведение данных чисел.
# user_input_1 = int(input("Input first num: "))
# user_input_2 = int(input("Input second num: "))
# print(f"This is sum of nums: {user_input_1 + user_input_2}")
# print(f"This is multiplication of nums: {user_input_1 * user_input_2}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит число. Выведите на экран квадрат этого числа, куб этого числа.
# user_input = int(input("Input num: "))
# print(f"Число в квадрате: {user_input ** 2}")
# print(f"power of three: {user_input ** 3}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Даны две переменных с некоторыми значениями. Поменять местами значения этих переменных
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит три числа.
# Увеличьте первое число в два раза, второе число уменьшите на 3,
# третье число возведите в квадрат и затем найдите сумму новых трех чисел.
# user_input_1 = int(input("Input first num: "))
# user_input_2 = int(input("Input second num: "))
# user_input_3 = int(input("Input third num: "))
#
# result_1 = user_input_1 * 2
# result_2 = user_input_2 - 3
# result_3 = user_input_3 ** 2
#
# print(f"Result is: {result_1 + result_2 + result_3}")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит три числа.
# Найдите среднее арифметическое этих чисел,
# а также разность удвоенной суммы первого и третьего чисел и утроенного второго числа.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Conditions -----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# Дано два числа. Вывести наибольшее из них.
# user_input_1 = int(input("Input first num: "))
# user_input_2 = int(input("Input second num: "))
#
# if user_input_1 > user_input_2:
#     print(f"max num is: {user_input_1}")
# else:
#     print(f"max num is: {user_input_2}")

# print(f"Max num is: {max([user_input_1, user_input_2])}")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Дано число. Если оно больше 3, то увеличить число на 10, иначе уменьшить на 10.
# user_balance = int(input("Input first num: "))
#
# if user_balance > 1_000_000:
#     print(f"result: {user_balance + 100_000}")
# elif user_balance == 1_000_000:
#     print(f"result: {user_balance * 10}")
# else:
#     print(f"result: {user_balance - 100_000}")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит номер месяца, вывести название месяца.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Loops  ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит ненулевые целые числа до тех пор, пока не введет ноль.
# Найдите количество четных чисел, которые он ввел.
# user_input = int(input("input number, but for exit input ZERO!"))
# even_count = 0
#
# while True:
#     if user_input == 0:
#         break
#     elif user_input % 2 == 0:
#         print("This is even number :)")
#         even_count += 1
#
#     user_input = int(input("input number, but for exit input ZERO!"))
#
# print(f"You have input even nums: {even_count}")

# a = "Sdsdsd_DSDSD_sdsd"
#
# for i in a:
#     if i.isupper():
#         print("This is UPPER letter :)")
#         continue
#
#     print(f"Result: {i + i}")



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Реализуйте серию из n игр "Камень, ножницы, бумага" с компьютером.
# В результате выведите статистику: сколько игр выиграл пользователь,
# сколько раз каждого вида ходов было сделано.
# ---------------------------------------------------------------------------------------------------
# Дополните игру анализом компьютера ваших ходов и выбор наиболее подходящего против вас хода.

# import random
#
# games_count = int(input("How many games do you wanna play? (please input number): "))
# print(f"Ok, you are about to play {games_count} games...")
# print("Please enter for Rock: 0, Paper: 1, Scissors: 2")
#
# user_wins = 0
# rock_count = 0
# paper_count = 0
# scissors_count = 0
#
# while games_count != 0:
#
#     print(f"rock_count: {rock_count}")
#     print(f"paper_count: {paper_count}")
#     print(f"scissors_count: {scissors_count}")
#
#     user_input = int(input("Please make your choice: "))
#
#     if rock_count == 0 and paper_count == 0 and scissors_count == 0:
#         comp_choice = random.randint(0, 2)
#     else:
#         pass
#
#     if user_input == 0:
#         rock_count += 1
#         if user_input == comp_choice or comp_choice == 1:
#             pass
#         else:
#             user_wins += 1
#             continue
#         games_count -= 1
#
#     elif user_input == 1:
#         paper_count += 1
#         if user_input == comp_choice or comp_choice == 2:
#             pass
#         if comp_choice == 0:
#             user_wins += 1
#             continue
#         games_count -= 1
#
#     elif user_input == 2:
#         scissors_count += 1
#         if user_input == comp_choice or comp_choice == 0:
#             pass
#         if comp_choice == 1:
#             user_wins += 1
#             continue
#         games_count -= 1
#
#     else:
#         print("Please input correct value: (0,1,2)")
#
#
# print(f"You won {user_wins} times")
# print(f"Rock was chosen: {rock_count} times")
# print(f"Paper was chosen: {paper_count} times")
# print(f"Scissors was chosen: {scissors_count} times")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит положительное целое число. Зашифровать каждую цифру серией из букв
# (конкретный принцип составления серии букв разработать самостоятельно).

user_input = input("Input number please: ")

encoded_password = ""

for i in user_input:
    for j in str(ord(i)):
        encoded_password += chr(int(j) + 65)

print(encoded_password)
