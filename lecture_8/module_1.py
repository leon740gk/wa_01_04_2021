from helper import attr_cutter

# print(f"top of module 1 (__name__): {__name__}")
# print(f"top of module 1 (dir()): {attr_cutter(dir())}\n")
def function_1_m1():
    print(f"I'm {function_1_m1.__name__} in module {__name__}")

# print(f"before import module 1 (__name__): {__name__}")
# print(f"before import module 1 (dir()): {attr_cutter(dir())}\n")
from module_2 import function_2_m2
# print(f"after import module 1 (__name__): {__name__}")
# print(f"after import module 1 (dir()): {attr_cutter(dir())}\n")

def function_2_m1():
    print(f"I'm {function_2_m1.__name__} in module {__name__}")

# if __name__ == '__main__':
function_2_m2()
# print(f"bottom of module 1 (__name__): {__name__}")
# print(f"bottom of module 1 (dir()): {attr_cutter(dir())}\n")
