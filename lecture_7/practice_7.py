# # Iterator / Iterable / Generator ============================================
# # https://nvie.com/posts/iterators-vs-generators/
#
# # Generator functions ========================================================
# # A simple generator function ------------------------------------------------
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n
#
#     n += 1
#     print('This is printed second')
#     yield n
#
#     n += 1
#     print('This is printed at last')
#     yield n
#
# # It returns an object but does not start execution immediately
# a = my_gen()
# # We can iterate through the items using next()
# next(a) # ..... to StopIteration
#
# # Using for loop
# for item in my_gen():
#     print(item)
#
# # A bit more -----------------------------------------------------------------
# # Let's take an example of a generator that reverses a string
# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length - 1, -1, -1):
#         yield my_str[i]
#
# # # For loop to reverse the string
# for char in rev_str("hello"):
#     print(char)
#
#
# # Generator expressions ======================================================
# Initialize the list
# my_list = [1, 3, 6, 10]

# square each term using list comprehension
# list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
# generator_ = (x**2 for x in my_list)
#
# print(list_)
# print(generator_)
#
#
# # Generator expressions can be used as function arguments.
# # When used in such a way, the round parentheses can be dropped.
# max(x**2 for x in my_list)
# sum(x**2 for x in my_list)
#
#
# # Why generators ? ===========================================================
# # # 1. Easy to implement: ------------------------------------------------------
# def pow_two_gen(max=0):
#     n = 0
#     while n < max:
#         yield 2 ** n
#         print("this is after yield")
#         n += 1
#
# # The same as above but with class implementation
# # class PowTwo:
# #     def __init__(self, max=0):
# #         self.n = 0
# #         self.max = max
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         if self.n > self.max:
# #             raise StopIteration
# #
# #         result = 2 ** self.n
# #         self.n += 1
# #         return result
#
# # 2. Memory Efficient: -------------------------------------------------------
# # A normal function to return a sequence will create
# # the entire sequence in memory before returning the result.
# # This is an overkill, if the number of items in the sequence is very large.
#
# # Generator implementation of such sequences is memory friendly
# # and is preferred since it only produces one item at a time.
#
# def num_printer(nums):
#     for i in nums:
#         print(i)
#
# nums_list = [x for x in range(100)]
# nums_generator = (x for x in range(100))
#
# # 3. Represent Infinite Stream: ----------------------------------------------
# # Generators are excellent mediums to represent an infinite stream of data.
# # Infinite streams cannot be stored in memory, and since generators
# # produce only one item at a time,
# # they can represent an infinite stream of data.
#
# # The following generator function can generate
# # all the even numbers (at least in theory).
# def all_even():
#     A = False
#     T = False
#     C = False
#     D = False
#     n = 0
#     while True:
#         # some logic here
#         yield n
#         n += 2
#
#
# # 4. Pipelining Generators ---------------------------------------------------
# # Multiple generators can be used to pipeline a series of operations.
# # This is best illustrated using an example.
# #
# # Suppose we have a generator that produces the numbers in the Fibonacci series.
# # And we have another generator for squaring numbers.
# #
# # If we want to find out the sum of squares of numbers in the Fibonacci series,
# # we can do it in the following way by pipelining the output of generator functions together.
#
# def fibonacci_numbers(nums):
#     x, y = 0, 1
#     for _ in range(nums):
#         x, y = y, x + y
#         yield x
#
# def square(nums):
#     for num in nums:
#         yield num**2
#
# print(sum(square(fibonacci_numbers(100))))
#
#
# # Coroutines =================================================================
# # https://www.geeksforgeeks.org/coroutine-in-python/
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)
#
# # calling coroutine, nothing will happen
my_coroutine = print_name("Dear")
#
# # This will start execution of coroutine and
# # Prints first line "Searching prefix..."
# # and advance execution to the first yield expression
my_coroutine.__next__()
# or next(my_coroutine)
#
# # sending inputs
# my_coroutine.send("Alex")
# my_coroutine.send("Dear Alex")
#
# # Closing a Coroutine --------------------------------------------------------
# def print_name(prefix):
#     print("Searching prefix:{}".format(prefix))
#     try:
#         while True:
#             name = (yield)
#             if prefix in name:
#                 print(name)
#     except GeneratorExit:
#         print("Closing coroutine!!")
#
#
# my_coroutine = print_name("Dear")
# my_coroutine.__next__()
# my_coroutine.send("Alex")
# my_coroutine.send("Dear Alex")
# my_coroutine.close()
#
#
# # Coroutines pipeline --------------------------------------------------------
#
#
# # Принять предложение в виде строки, разбить его на подстроки по пробелам
# # и каждое слово, к котором есть подстрока "ing" вывести в стандартный поток вывода
#
# # Function based solution
#
#
# def printer(word):
#     print(word)
#
#
# def string_filter(word, pattern="ing"):
#     if pattern in word:
#         printer(word)
#
#
# def producer(sentence: str):
#     words = sentence.split(" ")
#     for word in words:
#         string_filter(word)
#
# # Coroutines based solution
# def producer(sentence: str, next_coroutine):
#     """
#     Producer which just split strings and
#     feed it to pattern_filter coroutine
#     :param sentence: string
#     :param next_coroutine: generator
#     :return: None
#     """
#
#     tokens = sentence.split(" ")
#     for token in tokens:
#         next_coroutine.send(token)
#     next_coroutine.close()
#
# def pattern_filter(pattern="ing", next_coroutine=None):
#     """
#     Search for pattern in received token
#     and if pattern got matched, send it to
#     print_token() coroutine for printing
#     :param pattern: str
#     :return: None
#     """
#     print("Searching for {}".format(pattern))
#     try:
#         while True:
#             token = (yield)
#             if pattern in token:
#                 next_coroutine.send(token)
#     except GeneratorExit:
#         print("Done with filtering!!")
#
# def print_token():
#     """
#     Act as a sink, simply print the
#     received tokens
#     :return: None
#     """
#     print("I'm sink, i'll print tokens")
#     try:
#         while True:
#             token = (yield)
#             print(token)
#     except GeneratorExit:
#         print("Done with printing!")
#
# pt = print_token()
# pt.__next__()
# pf = pattern_filter(next_coroutine = pt)
# pf.__next__()
#
# sentence = "Bob is running behind a fast moving car"
# producer(sentence, pf)
#
#
