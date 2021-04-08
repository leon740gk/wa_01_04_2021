# Реализуйте серию из n игр "Камень, ножницы, бумага" с компьютером.
# В результате выведите статистику: сколько игр выиграл пользователь,
# сколько раз каждого вида ходов было выбрано.
# Дополните игру анализом компьютера ваших ходов и выбор наиболее подходящего против вас хода.

# import random
#
# games_number = int(input("How many games should we play? --> "))
# print(f"Ok, you have {games_number} tries to beat me :)")
# print("Rules: before each game please input on of:")
# print("0 - Rock;")
# print("1 - Paper;")
# print("2 - Scissors;")
# print("For exit game please input: 9")
# print("Ready? Let's start!")
#
# user_wins = 0
# rock_chosen = 0
# paper_chosen = 0
# scissors_chosen = 0
# user_choice = 0
#
# while user_choice != 9 and games_number != 0:
#     """
#     Here put the logic for simple ML
#     """
#     user_choice = int(input("Your turn: "))
#     computer_choice = random.randint(0, 2)
#     if user_choice == 0:
#         rock_chosen += 1
#         if computer_choice == user_choice or computer_choice == 1:
#             pass
#         else:
#             user_wins += 1
#         games_number -= 1
#
#     elif user_choice == 1:
#         paper_chosen += 1
#         if computer_choice == user_choice or computer_choice == 2:
#             pass
#         else:
#             user_wins += 1
#         games_number -= 1
#
#     elif user_choice == 2:
#         scissors_chosen += 1
#         if computer_choice == user_choice or computer_choice == 0:
#             pass
#         else:
#             user_wins += 1
#         games_number -= 1
#
#     elif user_choice == 9:
#         print("It's pity you wanna quit")
#         break
#
#     else:
#         print("please, input valid number (0, 1, 2)")
#
# print(f"User won {user_wins} times")
# print(f"Rock choices: {rock_chosen} times")
# print(f"Paper choices: {paper_chosen} times")
# print(f"Scissors choices: {scissors_chosen} times")



# Пользователь вводит положительное целое число. Зашифровать каждую цифру серией из букв
# (конкретный принцип составления серии букв разработать самостоятельно).

# user_input = input("Input number for encode: ")
# code_chars = ""
# for digit in user_input:
#     for x in str(ord(digit)):
#         code_chars += chr(int(x) + 65)
#
# print(code_chars)
#
# """
# Create decode implementation
# """