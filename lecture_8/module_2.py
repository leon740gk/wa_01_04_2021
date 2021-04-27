from helper import attr_cutter

# print(f"top of module 2 (__name__): {__name__}")
# print(f"top of module 2 (dir()): {attr_cutter(dir())}\n")
def function_1_m2(a, b):
    print(f"I'm {a} in module {b}")

# print(f"before import module 2 (__name__): {__name__}")
# print(f"before import module 2 (dir()): {attr_cutter(dir())}\n")
from module_1 import function_1_m1
# print(f"after import module 2 (__name__): {__name__}")
# print(f"after import module 2 (dir()): {attr_cutter(dir())}\n")

def function_2_m2():
    print(f"I'm {function_2_m2.__name__} in module {__name__}")

# if __name__ == '__main__':
function_1_m1()
# print(f"bottom of module 2 (__name__): {__name__}")
# print(f"bottom of module 2 (dir()): {attr_cutter(dir())}\n")
