# # Classes and instances (objects) ============================================
# # https://realpython.com/python3-object-oriented-programming/
# # https://www.geeksforgeeks.org/python-classes-and-objects/
#
#
#
# # OOP principles =============================================================
# # Polymorphism and magic methods ---------------------------------------------
# # https://www.geeksforgeeks.org/dunder-magic-methods-python/
#
# # # declare our own string class
# class MyString:
#     # magic method to initiate object
#     def __init__(self, string):
#         self.string = string
#
#     def __str__(self):
#         return "Object: {}".format(self.string)
#
    # def __add__(self, other):
    #     return self.string + other.string
#
#     def __gt__(self, other):
#         return len(self.string) > len(other.string)
#
#     def __ge__(self, other):
#         return len(self) >= len(other)
#
#     def __len__(self):
#         counter = 0
#         for _ in self.string:
#             counter += 1
#
#         return counter
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n < len(self.string):
#             return_value = self.string[self.n]
#             self.n += 1
#             return return_value
#         else:
#             raise StopIteration
#
# my_string = MyString("This is madness!")
# ordinary_string = "This is Sparta !!! :)"
#
# result_concat = my_string + ordinary_string
# print(result_concat)
# # Output: 'This is madness!This is Sparta !!! :)'
#
# result_compare = my_string > ordinary_string
# print(result_compare)
# # Output: False
#
#
# # Inheritance and multiple inheritance ---------------------------------------
# # https://www.geeksforgeeks.org/inheritance-in-python/
# # A Python program to demonstrate inheritance
#
# # Base or Super class. Note object in bracket.
# # (Generally, object is made ancestor of all classes)
# # In Python 3.x "class Person" is
# # equivalent to "class Person(object)"
# class Person:
#
#     # Constructor
#     def __init__(self, name):
#         self.name = name
#
#     # To get name
#     def get_name(self):
#         return self.name
#
#     # To check if this person is an employee
#     def is_employee(self):
#         return False
#
# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):
#
#     def __init__(self, name, salary):
#         Person.__init__(name)
#         self.salary = salary
#
#     def is_employee(self):
#         return True
#
#     def tell_about_duties(self):
#         print("Just doing some stuff")




# # Driver code
# emp = Person("Alex")  # An Object of Person
# print(emp.get_name(), emp.is_employee())
#
# emp = Employee("Gregor")  # An Object of Employee
# print(emp.get_name(), emp.is_employee())
#
# # ----------------------------------------------------------------------------
# # Python code to demonstrate how parent constructors
# # are called.
#
# # # parent class
# class Person:
#     # __init__ is known as the constructor
#     def __init__(self, name, id_number):
#         self.name = name
#         self.id_number = id_number
#
#     def display(self):
#         print(self.name)
#         print(self.id_number)
#
#
# # child class
# class Employee(Person):
#
#     def __init__(self, name, id_number, salary, duties):
#         Person.__init__(self, name, id_number)
#         self.salary = salary
#         self.duties = duties
#
#     def display(self):
#         Person.display(self)
#         print(self.salary)
#         print(self.duties)

#
# # creation of an object variable or an instance
# a = Employee('Gideon', 886012, 200000, "Intern")
#
# # calling a function of the class Person using its instance
# a.display()
#
# # Multiple inheritance -------------------------------------------------------
# # Python example to show the working of multiple
# # inheritance

# class Base1:
#     def __init__(self):
#         self.str1 = "This is madness"
#         print("Base1")
#
#     def method_1(self):
#         print("I'm method of the first base class")
#
#
# class Base2:
#     def __init__(self):
#         self.str2 = "This is Sparta !!!"
#         print("Base2")
#
#     def method_2(self):
#         print("I'm method of the second base class")
#
#
# class Derived(Base1, Base2):
#     def __init__(self):
#         # Calling constructors of Base1
#         # and Base2 classes
#         Base1.__init__(self)
#         Base2.__init__(self)
#         self.str3 = "This is string in child class"
#         print("Derived")
#
#     def print_strings(self):
#         print(self.str1, self.str2, self.str3 )
# #
#
# ob = Derived()
# ob.print_strings()
#
# # Multilevel inheritance -----------------------------------------------------
# # A Python program to demonstrate inheritance
#
# # Base or Super class. Note object in bracket.
# # (Generally, object is made ancestor of all classes)
# # In Python 3.x "class Person" is
# # equivalent to "class Person(object)"
# # !!!!!!!! ---------------------------------
# # builtins class object, class tuple(object)
# # __hash__ so on so forth ...
# class Base:
#
#     # Constructor
#     def __init__(self, name):
#         self.name = name
#
#     # To get name
#     def get_name(self):
#         return self.name
#
# class Child(Base):
#
#     # Constructor
#     def __init__(self, name, age):
#         Base.__init__(self, name)
#         self.age = age
#
#     # To get name
#     def get_age(self):
#         return self.age
#
#
# # Inherited or Sub class (Note Person in bracket)
# class GrandChild(Child):
#
#     # Constructor
#     def __init__(self, name, age, address):
#         Child.__init__(self, name, age)
#         self.address = address
#
#     # To get address
#     def get_address(self):
#         return self.address
#
# g = GrandChild("Alex", 35, "Kiev")
# print(g.get_name(), g.get_age(), g.get_address())
#
#
#
# # Encapsulation ==============================================================
# # https://www.geeksforgeeks.org/access-modifiers-in-python-public-private-and-protected/
#
# # program to illustrate public access modifier in a class
# class Geek:
#
#     # constructor
#     def __init__(self, name, age):
#         # public data members
#         self.geek_name = name
#         self.geek_age = age
#
#     # public member function
#     def display_age(self):
#         # accessing public data member
#         print("Age: ", self.geek_age)
#
#
# # creating object of the class
# obj = Geek("Alex", 20)
#
# # accessing public data member
# print("Name: ", obj.geek_name)
#
# # calling public member function of the class
# obj.display_age()

# # ----------------------------------------------------------------------------
# # program to illustrate protected access modifier in a class
# # super class
# class Student:
#     # protected data members
#     _name = None
#     _roll = None
#     _branch = None
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch
#
#     # protected member function
#     def _display_roll_and_branch(self):
#         # accessing protected data members
#         print("Roll: ", self._roll)
#         print("Branch: ", self._branch)

# # derived class
# class Geek(Student):
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         Student.__init__(self, name, roll, branch)
#
#     # public member function
#     def display_details(self, access_rights=None):
#         # accessing protected data members of super class
#         print("Name: ", self._name)
#         if access_rights == "Teacher":
#             # accessing protected member functions of super class
#             self._display_roll_and_branch()
#
# # creating objects of the derived class
# obj = Geek("Alex", 1706256, "Information Technology")
#
# # calling public member functions of the class
# obj.display_details()
#

# class A:
#     a = 4
#
#     def _a(self):
#         print("4")
#
#
# class B:
#     b = 7
#
#     def _b(self):
#         print("7")
#
#
# a = A()
# b = B()
#
# in_a = input("A")
# in_b = input("B")
#
# a.input = in_a
# b.input = in_b




# # ----------------------------------------------------------------------------
# # program to illustrate private access modifier in a class
# class Geek:
#     # private members
#     __name = None
#     __roll = None
#     __branch = None
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         self.__name = name
#         self.__roll = roll
#         self.__branch = branch
#         self.access_list = ["jdkfhbvjdf"]
#
#     # private member function
#     def __display_details(self):
#         # accessing private data members
#         print("Name: ", self.__name)
#         print("Roll: ", self.__roll)
#         print("Branch: ", self.__branch)
#
#     def _check_access(self, user):
#         if user.token in self.access_list:
#             return True
#         return False
#
#     # public member function
#     def access_private_function(self, user):
#         self._check_access(user)
#         # accessing private member function
#         self.__display_details()



# # creating object
# obj = Geek("Alex", 1706256, "Information Technology")
#
# # calling public member function of the class
# obj.access_private_function()





# # all together ---------------------------------------------------------------
# # program to illustrate access modifiers of a class
# # Show vars names conventions:
# # https://en.wikipedia.org/wiki/Naming_convention_(programming)
#
# super class
# class SuperClass:
#     # public data member
#     var1 = None
#
#     # protected data member
#     _var2 = None
#
#     # private data member
#     __var3 = None
#
#     # constructor
#     def __init__(self, var1, var2, var3):
#         self.var1 = var1
#         self._var2 = var2
#         self.__var3 = var3
#
#     # public member function
#     def display_public_members(self):
#         # accessing public data members
#         print("Public Data Member: ", self.var1)
#
#     # protected member function
#     def _displayProtectedMembers(self):
#         # accessing protected data members
#         print("Protected Data Member: ", self._var2)
#
#     # private member function
#     def __displayPrivateMembers(self):
#         # accessing private data members
#         print("Private Data Member: ", self.__var3)
#
#     # public member function
#     def accessPrivateMembers(self):
#         # accessing private member function
#         self.__displayPrivateMembers()
#
# # derived class
# class Sub(SuperClass):
#
#     # constructor
#     def __init__(self, var1, var2, var3):
#         SuperClass.__init__(self, var1, var2, var3)
#
#     # public member function
#     def accessProtectedMembers(self):
#         # accessing protected member functions of super class
#         self._displayProtectedMembers()
#
#
# obj = Sub("Geeks", 4, "Geeks !")
#
# # calling public member functions of the class
# obj.display_public_members()
# obj.accessProtectedMembers()
# obj.accessPrivateMembers()
#
# # Object can access protected member
# print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)
#
# # Private with inheritance ---------------------------------------------------
# # Python program to demonstrate private members
# # of the parent class
# class C(object):
#     def __init__(self):
#         self.c = 21
#
#         # d is private instance variable
#         self.__d = 42
#
#
# class D(C):
#     def __init__(self):
#         self.e = 84
#         C.__init__(self)
#
#
# object1 = D()
#
# # produces an error as d is private instance variable
# print(object1.__d)
#
#
# # Inheritance vs Composition =================================================
# # https://realpython.com/inheritance-composition-python/
#
#
# # Method's decorators ========================================================
# # https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
# # https://www.tutorialsteacher.com/python/property-function
# # https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python
# # https://pythonguide.readthedocs.io/en/latest/python/property.html
#
# # staticmethod and class method ----------------------------------------------
# # https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
#
# class Date:
#
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 2099
#
# input_dates_data = ['11-05-2012', '11-07-2012', '11-09-2022', '11-09-2045875648']
# new_objects = []
#
# for i in input_dates_data:
#     if Date.is_date_valid(i):
#         date_obj = Date.from_string(i)
#         new_objects.append(date_obj)
#
#
# # Property -------------------------------------------------------------------
# # https://www.tutorialsteacher.com/python/property-function
#
# class Person:
#     def __init__(self):
#         self.__name=''
#
#     def set_name(self, name, access_rights=None):
#         if access_rights == "SuperUser":
#             self.__name=name
#         else:
#             print("You have no rights for that")
#
#     def get_name(self):
#         print('get_name() called')
#         return self.__name
#
#     name = property(get_name, set_name)


# # https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python
# class Money:
#     def __init__(self, dollars, cents):
#         self.__total_cents = dollars * 100 + cents
#
#     # Getter and setter for dollars...
#     @property
#     def dollars(self):
#         print("dollar getter")
#         return self.__total_cents // 100
#
#     @dollars.setter
#     def dollars(self, new_dollars):
#         # make some validation
#         print("dollar setter")
#         self.__total_cents = 100 * new_dollars + self.cents
#
#     # And the getter and setter for cents.
#     @property
#     def cents(self):
#         print("cents getter")
#         return self.__total_cents % 100
#
#     @cents.setter
#     def cents(self, new_cents):
#         # make some validations
#         print("cents setter")
#         self.__total_cents = 100 * self.dollars + new_cents


# # MRO, super(), __slots__ ====================================================
# # MRO ------------------------------------------------------------------------
# # https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/
# # https://habr.com/ru/post/62203/ <<<<<<------------------------ long story
# # https://coderoad.ru/54867/%D0%92-%D1%87%D0%B5%D0%BC-%D1%80%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B0-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B0%D0%BC%D0%B8-%D1%81%D1%82%D0%B0%D1%80%D0%BE%D0%B3%D0%BE-%D1%81%D1%82%D0%B8%D0%BB%D1%8F-%D0%B8-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D1%81%D1%82%D0%B8%D0%BB%D1%8F-%D0%B2-Python
#
# class A:
#     def foo_1(self):
#         print(" In class A")
#
# class B(A):
#     def foo_2(self):
#         print(" In class B")
#
# class C(A):
#     def foo_3(self):
#         print("In class C")
#
# class D(B, C):
#     pass

# # it prints the lookup order
# print(D.__mro__)
# print(D.mro())
#
#
# # super() --------------------------------------------------------------------
# # https://www.programiz.com/python-programming/methods/built-in/super
# # https://realpython.com/python-super/

# class Animal:
#     def __init__(self, Animal):
#         print(Animal, 'is an animal.')
#
# class Mammal(Animal):
#     def __init__(self, mammalName):
#         print(mammalName, 'is a warm-blooded animal.')
#         super().__init__(mammalName)
#
# class NonWingedMammal(Mammal):
#     def __init__(self, NonWingedMammal):
#         print(NonWingedMammal, "can't fly.")
#         super().__init__(NonWingedMammal)
#
# class NonMarineMammal(Mammal):
#     def __init__(self, NonMarineMammal):
#         print(NonMarineMammal, "can't swim.")
#         super().__init__(NonMarineMammal)
#
# class Cat(NonMarineMammal, NonWingedMammal):
#     def __init__(self):
#         print('Cat has 4 legs.');
#         super().__init__('Cat')
#
#
# d = Cat()
# print('')
# bat = NonMarineMammal('Bat')


# https://realpython.com/python-super/
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)
#
# class VolumeMixin:
#     def volume(self):
#         return self.area() * self.height
# 
# class Cube(VolumeMixin, Square):
#     def __init__(self, length):
#         Square.__init__(length)
#         self.height = length
#
#     def face_area(self):
#         return super().area()
#
#     def surface_area(self):
#         return super().area() * 6
