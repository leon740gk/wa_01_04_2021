# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Реализуйте серию из n игр "Камень, ножницы, бумага" с компьютером.
# В результате выведите статистику: сколько игр выиграл пользователь,
# сколько раз каждого вида ходов было сделано.
# ---------------------------------------------------------------------------------------------------
# Дополните игру анализом компьютера ваших ходов и выбор наиболее подходящего против вас хода.

import random

games_count = int(input("How many games do you wanna play? (please input number): "))
print(f"Ok, you are about to play {games_count} games...")
print("Please enter for Rock: 0, Paper: 1, Scissors: 2")

user_wins = 0
rock_count = 0
paper_count = 0
scissors_count = 0

while games_count != 0:

    print(f"rock_count: {rock_count}")
    print(f"paper_count: {paper_count}")
    print(f"scissors_count: {scissors_count}")

    user_input = int(input("Please make your choice: "))

    if rock_count == 0 and paper_count == 0 and scissors_count == 0:
        comp_choice = random.randint(0, 2)
    else:
        pass
        # Here should be logic for computer decisions based on user picks

    if user_input == 0:
        rock_count += 1
        if user_input == comp_choice or comp_choice == 1:
            pass
        else:
            user_wins += 1
            continue
        games_count -= 1

    elif user_input == 1:
        paper_count += 1
        if user_input == comp_choice or comp_choice == 2:
            pass
        if comp_choice == 0:
            user_wins += 1
            continue
        games_count -= 1

    elif user_input == 2:
        scissors_count += 1
        if user_input == comp_choice or comp_choice == 0:
            pass
        if comp_choice == 1:
            user_wins += 1
            continue
        games_count -= 1

    else:
        print("Please input correct value: (0,1,2)")


print(f"You won {user_wins} times")
print(f"Rock was chosen: {rock_count} times")
print(f"Paper was chosen: {paper_count} times")
print(f"Scissors was chosen: {scissors_count} times")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит положительное целое число. Зашифровать каждую цифру серией из букв
# (конкретный принцип составления серии букв разработать самостоятельно).

user_input = input("Input number please: ")
encoded_password = ""

for i in user_input:
    for j in str(ord(i)):
        encoded_password += chr(int(j) + 65)

print(encoded_password)
# Create decoding logic for password