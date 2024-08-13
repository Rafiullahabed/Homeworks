
# 1- abs()  Returns the absolute of a number
# x = abs(-8.43)
# print(x)   # output: 8.43

# 2- all()  Returns True if all items in an iterable object are true
# mylist = [True,True,True]
# x = all(mylist)
# print(x) # output: True

# 3- any()  Returns True if any item in an iterable object is true
# mylist = [True, False, False]
# x = any(mylist)
# print(x) # output: True

# 4- ascii()  Returns a readable version of an object. Replaces none-ascii characters with
# escape character
# x = ascii("My name is SӇle")
# print(x) # output: 'My name is S\u04c7le

# 5- bin() Returns the binary version of a number
# print(bin(56))  # output: 0b111000

# 6- bool() Returns the boolean value of the specificed object
# print(bool(1)) # output: True

# 7- bytearray() Returns an arry of byte
# print(bytearray(4)) # output: bytearray(b'\x00\x00\x00\x00')

# 8- bytes()  Returns a bytes of object
# print(bytes(4))  # output: b'\x00\x00\x00\x00'

# 9- callable() Returns Tru if the specified object is callable, otherwise False
# def z():
#     a = 5
# print(callable(z)) # output: True

# 10- chr() Returns a character from the specified Unicode code
# print(chr(43))  # output: +

# 11- classmethod() Converts a method into a class method
# class C:
#     def f(cls, arg1, arg2): ...
#     classmethod(f)

# 12- compile() Reurns the specified source as an object, ready to be executed
# x = compile('print(55)','test', 'eval')
# exec(x)  # output: 55

# 13- complex() Returns a comples number 
# print(complex(4,5)) # output: (4+5j)

# 14- delatt() Deletes the specified attribute (property of method) from the specified object
# class Person:
#     name = "Ahmad"
#     age = 23
#     country = "Afghanistan"
# delattr(Person,"age")

# 15- dict()  Returns a dictionary (Array)
# x = dict(name="Ahmad", age=24, country="Afghanistan")
# print(x)  # output: {'name': 'Ahmad', 'age': 24, 'country': 'Afghanistan'}

# 16- dir() Returns a list of the specified object's properties and methods
# class Person:
#     name = "Ahmad"
#     age = 23
#     country = "Afghanistan"
# print(dir(Person))

# 17- divmod() Returns the quotient  and the remainder when argument1 is divided by argument
# x = divmod(5,2)
# print(x) # output: (2, 1)

# 18- enumerate() Takes a collection (e.g. a tuple) and returns it as an enumerate object
# x = ("apple", "banana", "cherry")
# y = enumerate(x)
# print(list(y)) # output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# 19- eval() Returns Evaluates and executes an expression
# x = "3+4-1"
# y = eval(x)
# print(y) # output: 6

# 20- exec() Executes the specified code (or object)
# x = 'name = "Ahmad" \nprint(name)'
# exec(x)  # output: Ahmad

# 21- filter()  Use a filter fanction to exclude items in an iterable object
# ages = [5,23,24,12,11,19,32]
# def myfanc(x):
#     if x < 18:
#         return False
#     else:
#         return True
# adults = filter(myfanc, ages)
# for i in adults:
#     print(i)

# 22- float()  Returns a floating point number
# x = float(3)
# print(x)  # output: 3.0

# 23- format()  Formats a specified value
# x = format(0.5, "%")
# print(x)  # output: 50.000000%

# 24- frozenset()  Returns a frozenset objec , Freeze the list and make it unchangeable
# lst = ["apple", "banana", "cherry"]
# x = frozenset(lst)
# print(x)  # output: frozenset({'banana', 'apple', 'cherry'})

# 25- getattr()   Returns the value of the specified object has the specified attribute (property/method)
# class Person:
#     name = "Ahmad"
#     age = 23
#     country = "Afghanistan"
# x = getattr(Person, "age")
# print(x)  # output: 23

# 26- globals()  Returns the current global symbol table as a dictionary
# x = globals()
# print(x)
# print(x["__file__"])

# 27- hasattr()  Returns True if the specified object has the specified attribute (property/method)
# class Person:
#     name = "Ahmad"
#     age = 23
#     country = "Afghanistan"
# x = hasattr(Person, "age")  
# print(x)  # output: True

# 28- hash()  Returns the hash value of a specified object
# x = hash(345)
# print(x)  # output: 345

# 29- help()  Executes the built in help system
# print(help())

# 30- hex()  Converts a number into a hexadecimal value
# print(hex(400)) # output: 0x190

# 31- id()  Returns the id of an object 
# x = "a name"
# print(id(x))  # output: 1988668970096

# 32- input()  Allowing user input
# name = input("Enter your name: ")
# print("Hello" + name)

# 33- int()  Returns an integer number
# print(int(43.32))  # output: 43

# 34- isinstance()  Retruns True if a specified object is an instance of a specified object
# x = isinstance(8, int)
# print(x)  # output: True

# 35- issubclass()  Returns True if a specified object is an instance of a specified object
# class Age:
#     age = 35
# class Obj(Age):
#     name = "Ahmad"
#     age = Age
# print(issubclass(Obj,Age))  # output: True

# 36- iter()  Returns an iterator object
# x = iter(["apple","banana","cherry"])
# print(next(x))  # output: apple
# print(next(x))  # output: banana
# print(next(x))  # output: cherry

# 37- len()  Returns the length of an object
# name = "Ahmad"
# print(len(name))  # output: 5

# 38- list()  Returns a list
# x = list(("apple", "banana", "cherry"))
# print(x)  # output: ['apple', 'banana', 'cherry']

# 39- locals()  Returns an updated dictionary of the current local symbol table
# x = locals()
# print(x)

# 40- map()  Returns the specified iterator with the specified function applied to each item
# def func(n):
#     return len(n)
# x = map(func, ("apple","banana", "cherry"))
# print(list(x))  # output: [5, 6, 6]

# 41- max()  Returns the largest item in an iterable
# print(max(34,65))  # output: 65

# 42- min()  Returns the smallest item in an iterable
# print(min(34,65))  # output: 34

# 43- memoryview()  Returns a memory view object
# x = memoryview(b"Ahmad")
# print(x)  # output: <memory at 0x0000025AA61A4940>
# print(x[0])  # output: 65

# 44- next()  Returns the next item in an iterable
# x = iter(["apple","banana","cherry"])
# print(next(x))  # output: apple
# print(next(x))  # output: banana
# print(next(x))  # output: cherry

# 45- object()  Returns a new object
# x = object()
# print(dir(x))

# 46- oct()  Converts a number into an octal
# print(oct(34534)) # output: 0o103346

# 47- open()  Opens a file and returns a file object
# file = open("demofile.txt", "a+")
# print(file.read())

# 48- ord()  Converts an integer represinting the Unicode of the specified character
# print(ord("y"))  # output: 121

# 49- pow()  Returns the value of x to the power of y
# print(pow(3,4)) # output: 81

# 50- print()  Prints to the standard ouput device
# print("Ahmad")  # output: Ahmad

# 51- property()  Gets, sets, deletes a property

# 52- range()  Returns a sequence of numbers, string from 0 and increments by 1 (by default)
# x = range(3)
# for n in x:
#     print(n)  # output: 0 \n 1 \n 2

# 53- repr()  Returns a readable version of an object
# class MyClass:
#     def __init__(self, name) -> None:
#         self.name = name

#     def __repr__(self) -> str:
#         return f"The name is {self.name}"
# obj = MyClass("Ahmad") 
# print(repr(obj))  # output: The name is Ahmad

# 54- reversed()  Returns a reversed iterator
# alph = [1,2,3,4,5]
# ralph = reversed(alph)
# print(list(ralph))  # output: [5, 4, 3, 2, 1]

# 55- round()  Rounds a number
# print(round(45.54556))  # output: 46

# 56- set()  Returns a new set object
# x = (("apple","banana","cherry"))
# print(x)  # output: ('apple', 'banana', 'cherry')

# 57- setattr()  Sets an attribute of an object
# class Person:
#     name = "Ahmad"
#     age = 23
#     country = "Afghanistan"
# setattr(Person,"age",34)

# 58- slice()  Returns a slice object
# a = (1,2,3,4,5,6)
# x = slice(3)
# print(a[x])  # output: (1, 2, 3)

# 59- sorted()  Returns a sorted object
# x = [4,5,1,6,1,0,6,7]
# rx= sorted(x)
# print(rx)  # output: [0, 1, 1, 4, 5, 6, 6, 7]

# 60- str()  Returns a string object
# x = str(4.3)
# print(x)  # output: 4.3

# 61- sum()  Sums the items of an iterator
# x = (1,2,3,4)
# s = sum(x)
# print(s)   # output: 10

# 62- super()  Returns an object that represents the parent class
# class Parent:
#     def __init__(self,txt) -> None:
#         self.message = txt
#     def printmessage(self):
#         print(self.message)
    
# class Child(Parent):
#     def __init__(self, txt) -> None:
#         super().__init__(txt)

# x = Child("Hello, and welcome!")
# x.printmessage()  # output: Hello, and welcome!

# 63- tuple()  Returns a tuple
# x = tuple(("apple","banana","cherry"))
# print(x)  # output: ('apple', 'banana', 'cherry')

# 64- vars()  Returns the __dict__ property of an object
# class Person:
#     name = "Ahmad"
#     age = 23
#     country = "Afghanistan"
# x = vars(Person)
# print(x)

# 65- type()  Returns the type of an object
# a = "Rafiullah"
# b = 45
# print(type(a))  # output: <class 'str'>
# print(type(b))  # output: <class 'int'>

# 66- zip()  Returns an iterator, from two or more iterators
# a = ("Rafiullah","Ahmad","karim")
# b = ("Abid", "amiry", "sharifi")
# z = zip(a,b)
# print(tuple(z))  # output: (('Rafiullah', 'Abid'), ('Ahmad', 'amiry'), ('karim', 'sharifi'))
