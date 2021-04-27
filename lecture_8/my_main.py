from mod_1 import adder
from bonus_helper import adder_with_bonus
import mod_2

a = int(input("Please enter 1st num: "))
b = int(input("Please enter 2nd num: "))

operator = input("Please input operator (+, *, - , /): ")

operator_mapper = {
    "+": adder,
    # "*": mod_1.mul,
    "-": mod_2.substraction,
    "/": mod_2.division,
}

function_to_call = operator_mapper.get(operator, adder_with_bonus)

if __name__ == "__main__":

    result = function_to_call(a, b)
    print(result)
