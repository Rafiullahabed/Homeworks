from dataclasses import dataclass, field
import datetime
import json
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from typing import Any
from tkinter import Frame
from configparser import ConfigParser 
import requests 


# Basic Class and Object Exercises
# 1- Create a class called Person with attributes name and age.
# and create an object of the class and print its attributes?
class Person:
    name = "Rafiullah"
    age = 19
# obj = Person()
# print(obj.name)
# print(obj.age)


# 2- Add a method called greet to the Person class that prints a greeting message including the person's name.
class Person:
    name = "Rafiullah"

    def greet(self):
        print(f"Welcome! I hope you were fine {self.name}")

# obj = Person()
# obj.greet()


# 3- Create a class called Car with attributes make, model, and year.
# include a method to print out the car's details.
class Car:
    make = "Canada"
    model = "toyota"
    year = 2006

    def show_details(self):
        print(f"maked by {self.make} , its model is {self.model} and generated in {self.year}")

# car = Car()
# car.show_details()


# 4- Create a class Circle with a method to compute the area. initialize the class with the redius.
class Circle:
    def __init__(self, redius):
        self.redius = redius

    def area(self):
        return 3.1415 * int(self.redius) ** 2
# circle = Circle(2)
# print(circle.area())


# 5- Create a Rectangle with methods to compute the area and perimeter.
# Intialize the class with the length and width.
class Rectangle:
    def __init__(self,length , width):
        self.length = length
        self.wigth = width

    def area(self):
        return self.length * self.wigth

    def perimeter(self):
        return 2 * (self.length + self.wigth)
# obj_rectangle = Rectangle(10 ,20)
# print(obj_rectangle.area())
# print(obj_rectangle.perimeter())


# Inheritance and Polymorphism Exercises
# 6- Create a base class Animal with a method speak.
# Create two derived classes Dog and Cat that override the speak method.
class Animal:
    def speak(self):
        print("Animal Speaks")


class Dog(Animal):
    def speak(self):
        print("The dog bark")


class Cat(Animal):
    def speak(self):
        print("The Cat meow")


# 7- Create a base class Shape with a method area.
# Create drived classes Square and Triangle  that implement the area method
class Shape:
    def __init__(self,**kwargs):
        for key , value in kwargs.items():
            setattr(self, key,value)
    def calculate_area(self):
        pass

class Triangle(Shape):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        return (self.base * self.height) / 2

class Square(Shape):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        return self.length ** 2


# 8- Create a class Employee with attributes name and salary.
# Create a derived class Manager with an additional attribute department
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department


# 9- Create a base class Vehicle with a method drive.
# Create derived classes Bike and Truck that override the drive method
class Vehicle:
    def drive(self):
        print("The vehicle is driving...")

class Bike(Vehicle):
    def drive(self):
        print("The bike is under riding...")

class Truck(Vehicle):
    def drive(self):
        print("The truck is under driving...")


# 10- Create a base class Bird with a method fly. Create derived classes Eagle and Penguin.
# Override the fly method in Penguin to indicate that penguins cannot fly.
class Bird:
    def fly(self):
        print("the bird is flying...")


class Eagle(Bird):
    def fly(self):
        print("The Eagle is flying...")


class Penguin(Bird):
    def fly(self):
        print("The Penguin can not fly.")



# Encapsulation and Abstraction Exercises
# 11- Create a class Account with private attributes balance.
# Provide public methods to deposit and withdraw money.
@dataclass
class Account:
    __name : str
    __balance = 0
    def deposit(self, deposit):
        self.__balance += deposit

    def withdraw(self, withdraw):
        self.__balance -= withdraw

a = Account("ahmad")
a.deposit(400)
print(a)


# 12- Create a class Book with private attributes title, author, and pages.
# Provide public methods to get and set these attributes.
class Book:
    __title = ""      # private attribute
    __author = ""     # private attribute
    __pages = 0       # private attribute
    def set_title(self,title):
        self.__title = title
    def set_author(self,author):
        self.__author = author
    def set_pages(self,pages):
        self.__pages = pages
    def get_title(self):
        print(self.__title)
    def get_author(self):
        print(self.__author) 
    def get_pages(self):
        print(self.__pages)



# 13- Create a class Laptop with private attributes brand, model, and price.
# Provide a method to apply a discount and a method to display laptop details.
class Laptop:
    def __init__(self,brand,model,price):
        self.__brand = brand
        self.__model = model
        self.__price = price
    discount = 10

    def show_detail(self):
        print(f"Details of laptop are: brand: {self.__brand}, model: {self.__model}, price: {self.__price}")

    def applying_discount(self):
        self.__price = (self.__price - (self.__price * (self.discount/100)))

a = Laptop("Dell","7390",15000)
a.applying_discount()
a.show_detail()


# 14- Create a class BankAccount with private attributes account_number and balance.
# Provide methods to deposit, withdraw, and check the balance.
class BankAcount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, deposit):
        self.__balance += deposit

    def withdraw(self, withdraw):
        self.__balance -= withdraw

    def check_balance(self):
        print(f"The balance is {self.__balance}")



# 15- Create a class Student with private attributes name, grade, and age.
# # Provide methods to get and set these attributes and a method to display the student's details.
class Student:
    __name = ""
    __grade = ""
    __age = 0
    def set_name(self,name):
        self.__name = name
    def set_grade(self,grade):
        self.__grade = grade
    def set_age(self,age):
        self.__age = age
    def get_name(self):
        print(self.__name)
    def get_grade(self):
        return self.__grade
    def get_age(self):
        return self.__age

    def sho_details(self):
        print(f"Name: {self._name}, Grade: {self._grade}, Age: {self._age}")


# Class Relationships and Advanced Concepts Exercises
# 16- Create a class Library with attributes name and books (a list of Book objects).
# Provide methods to add and remove books
@dataclass
class Library:
    name : str
    books : list

    def add_book(self,*args):
        for i in args:
            return self.books.append(i)
    def remove_book(self,*args):
        for i in args:
            return self.books.remove(i)


# 17- Create a class School with attributes name and students (a list of Student objects).
# Provide methods to add and remove students

@dataclass
class School:
    
    name : str  
    students = []
    def add_students(self, *args):
        for n in args:
            return self.students.append(n)

    def remove_students(self,*args):
        for i in args:
            return self.students.remove(i)



# 18- Create a class Team with attributes name and members (a list of Person objects).
# Provide methods to add and remove members
class Team:
    def __init__(self,name:str,*args):
        self.name = name
        self.members = list(args)

    def add_members(self, *args):
        for n in list(args):
            return self.members.append(n)

    def remove_members(self,*args):
        for i in args:
            return self.members.remove(i)



# 19- Create a class Company with attributes name and employees (a list of Employee objects).
# Provide methods to add and remove employees.
@dataclass
class Campany:
    name : str
    def __post_init__(self):
        self.employees = []

    def add_employees(self, *args):
        for n in list(args):
            return list(self.employees).append(n)

    def remove_employees(self,*args):
        for i in args:
            return self.employees.remove(i)



# 20- Create a class Zoo with attributes name and animals (a list of Animal objects).
# # Provide methods to add and remove animals
class Zoo:
    def __init__(self,name:str):
        self.name = name
        self.animals = []

    def add_animals(self, *args):
        for n in list(args):
            return self.animals.append(n)

    def remove_animals(self,*args):
        for i in args:
            return self.animals.remove(i)



# # 21- Create a class FileManager with methods to read from and write to a file.
class FileManager:
    def __init__(self,fileName):
        self.file_name = fileName
    def write_to_file(self,message):
        with open(self.file_name,"a") as file:
            file.write(message)

    def read_the_file(self):
        with open(self.file_name, "a+") as file:
            return file.readline()

c = FileManager("File.txt")
# c.write_to_file("the message was wrote")
print(c.read_the_file())



# 22. Create a class Log with methods to write error messages to a log file.
class Log:
    def __init__(self,file_name):
        self.file_name = file_name
    def write_error(self,message: str):
        with open(self.file_name,"a") as file:
            file.write(f"in {datetime.datetime.now().strftime('%Y-%m-%d %HH:%MM:%SS')}, there is an error: {message}\n")


# 23. Create a class Config that reads configuration settings from a file
# and provides methods to access these settings.
class Config:
    def __init__(self,filepath):
        self.filepath = filepath
        self.settings = self.read_config()

    def read_config(self):
        with open(self.filepath) as file:
            return json.load(file)

    def get(self,key,default = None):
        keys = key.split(".")
        value = self.settings
        for i in keys:
            value = value.get(i)
            if value is None:
                return default
            return value
# obj = Config("Json_file.json")
# obj.read_config()
# print(obj.get('logging.level'))



# 24. Create a class Database that connects to a database and provides methods to execute queries.
# Handle exceptions if the connection fails.
@dataclass
class Database:
    host : str
    user : str
    password : str
    database : str

    def __post_init__(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)
        self.cursor = self.connection.cursor()

    def exicute(self,query):
        self.cursor.execute(query)

# c = Database("localhost","root","","test")
# c.connector()
# print(c.__dict__)
# c.exicute("select * from student")







# 25. Create a class Report that generates a report from data in a file. Provide methods to handle
# exceptions if the file does not exist or cannot be read.
class Report:
    def __init__(self,filepath):
        self.filepath = filepath
        self.data = None

    def read_file(self):
        try:
            file = open(self.filepath)
            self.data = file.read()
            print("file opened successfuly.")
        except FileNotFoundError:
            print(f"The file: {self.filepath} is not exist")
            print(f"The file: {self.filepath} cannot read")

    def generate(self):
        if self.data == None:
            print("No data available to generate report.")
        else:
            print(f"Report generated:\n {self.data}")


# Real-world Application Exercises
# 26. Create a class Ticket for a movie theater with attributes movie_name, seat_number, and price.
# Provide methods to display ticket details and apply discounts.
@dataclass
class Ticket:
    movie_name : str
    seat_number : int
    price : float
    discount = 10

    def apply_discount(self):
        self.price = self.price - (self.price * (self.discount / 100))
    
    def __repr__(self):
        return f"move_name: {self.movie_name}, seat_number: {self.seat_number}, price:{self.price}"

# obj = Ticket("name",34,23.4)
# print(obj)


# 27. Create a class ShoppingCart with methods to add, remove, and display items. Each item should
# be an object of a class Item with attributes name and price.
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self,name,price):
        self.name = name
        self.price = price
        self.items.append(f"{name}: {price}")

    def remove_items(self):
        self.items.clear()

    def __str__(self):
        return f"List of items are: {self.items}"



# 28. Create a class Restaurant with attributes name and menu (a list of Item objects). Provide
# methods to add and remove items from the menu.

class Restaurant:
    def __init__(self,name):
        self.name = name
        self.menu = []

    def add_items(self,items:list):
        for i in items:
            self.menu.append(i)

    def remove_items(self,item):
        self.menu.remove(item)

    def __repr__(self):
        return f"The list of menu are: {self.menu}"



# 29. Create a class Flight with attributes flight_number, destination, and passengers (a list of Person
# objects). Provide methods to add and remove passengers.
class Flight:
    def __init__(self,flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = []

    def add_passengers(self,passengers:list):
        for i in passengers:
            self.passengers.append(i)

    def remove_passengers(self,passenger):
        self.passengers.remove(passenger)

    def __repr__(self):
        return f"Passengers are: {self.passengers}"



# 30. Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room
# should have attributes room_number and is_occupied. Provide methods to book and checkout rooms.
class Room:
    def __init__(self,room_number):
        self.room_number = room_number
        self.is_occupied = False

    def __str__(self):
        return f"Room {self.room_number} : {"occupied" if self.is_occupied else "abailable"}"

class Hotel:
        def __init__(self, name):
            self.name = name
            self.rooms = []

        def add_room(self, room_number):
            self.rooms.append(Room(room_number))

        def book_room(self,room_number):
            for room in self.rooms:
                if room.room_number == room_number:
                    if not room.is_occupied:
                        room.is_occupied = True
                        print(f"Room {room_number} has been booked")
                        return
                    else:
                        print(f"Room {room_number} already occupied")
                        return
            else:
                print(f"Room {room_number} does not exist")

        def check_out_room(self,room_number):
            for room in self.rooms:
                if room.room_number == room_number:
                    if room.is_occupied:
                        room.is_occupied = False
                        print(f"Room {room_number} has been checked out.")
                    else:
                        print(f"Room {room_number} is not occupied.")
                else:
                    print(f"Room {room_number} does not exist.")

        def display_rooms(self):
            for room in self.rooms:
                print(room)

# hotel = Hotel("kunduz")
# hotel.add_room("100")
# hotel.add_room("101")
# hotel.add_room("102")
# hotel.add_room("103")
#
# hotel.display_rooms()
#
# hotel.book_room("101")
# hotel.book_room("102")
#
# hotel.display_rooms()
#
# hotel.check_out_room("101")
#
# h = Hotel("kunduz")
# h.add_room("101")



# GUI Application Exercises
# 31. Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and
# decrement buttons.
class CounterApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Counter App")
        self.window.geometry("250x100")
        self.window.resizable(False,False)
        self.window.config(bg="black")
        self.count = 0
        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=1)
        self.label = tk.Label(self.window, text=0, font=("Arial",26),bg="black",fg="white")
        self.button1 = tk.Button(self.window, text="Increment", bg="green" ,command=self.counter)
        self.button2 = tk.Button(self.window, text="Decrement", bg="red",command=self.decrement)
        self.label.grid(row=0, column=0,columnspan=2)
        self.button2.grid(row=1, column=0)
        self.button1.grid(row=1,column=1)
        self.window.tk.mainloop()

    def counter(self):
        self.count += 1
        self.label.config(text = self.count)

    def decrement(self):
        self.count -= 1
        self.label.config(text=self.count)

# CounterApp()


# 32. Create a class ToDoApp that uses tkinter to create a to-do list GUI where users can add and remove tasks.
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.root.config(bg="gray")
        self.root.resizable(False,False)

        self.listbox = tk.Listbox(
            frame, width=50, height=10, bd=0, selectmode=tk.SINGLE,bg="black",fg="white")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(frame,bg="black")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.task_entry = tk.Entry(self.root, width=50, bg="gray",fg="white")
        self.task_entry.pack(pady=10)


        button_frame = tk.Frame(self.root,bg="gray")
        button_frame.pack(pady=10)

        self.add_task_button = tk.Button(
            button_frame, text="Add Task", command=self.add_task, bg="green")
        self.add_task_button.pack(side=tk.LEFT,padx=20)

        self.remove_task_button = tk.Button(
            button_frame, text="Remove Task", command=self.remove_task,bg="red")
        self.remove_task_button.pack(side=tk.LEFT, padx=20)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ToDoApp(root)
#     root.mainloop()


# 33. Create a class CalculatorApp that uses tkinter to create a simple calculator GUI.
class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x300")
        self.resizable(width=True,height=False)

        def button_click(item):
            current = input_text.get()
            input_text.set(current + item)

        def clear():
            input_text.set("")

        def evaluate():
            try:
                result = str(eval(input_text.get()))
                input_text.set(result)
            except Exception as e:
                input_text.set("Error")

        def dot():
            if "." not in input_field.get():
                btn.config(comman= button_click("."))



        input_text = tk.StringVar()
        input_frame = tk.Frame(self)
        input_frame.pack()
        input_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(input_frame, textvariable=input_text, font=("Arial", 24), bd=5,
                       bg="light grey")
        input_field.pack( expand=True, fill= "both")
        # input_field.pack(expand=True, fill="both")

        button_frame = tk.Frame(self)
        button_frame.pack(expand=True, fill="both")


        buttons = [
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+'
                ]

        row = 0
        col = 0

        for button in buttons:
            if button == '=':
                btn = tk.Button(button_frame, text=button, font=("Arial", 18), fg="black", bd=0, command=evaluate)
            elif button == 'C':
                btn = tk.Button(button_frame, text=button, font=("Arial", 18), fg="black", bd=0, command=clear)
            elif button == ".":
                btn = tk.Button(button_frame, text=button, font=("Arial", 18), fg="black", bd=0, command=dot)
            else:
                btn = tk.Button(button_frame, text=button, font=("Arial", 18), fg="black", bd=0,
                        command=lambda x=button: button_click(x))

            btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
            col += 1
            if col > 3:
                col = 0
                row += 1


        clear_button = tk.Button(button_frame, text='C', font=("Arial", 18), fg="black", bd=0, command=clear)
        clear_button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)


        for i in range(4):
                button_frame.columnconfigure(i, weight=1)
        for i in range(5):
                button_frame.rowconfigure(i, weight=1)
        self.mainloop()

# CalculatorApp()

# 34. Create a class LoginApp that uses tkinter to create a login form GUI.
class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LoginApp")
        self.geometry("800x580+0+0")
        self.resizable(False,False)


        def u_focusin(event):
            if self.user_name.get()=="Username":
                self.user_name.delete(0,tk.END)
            
        def p_focusin(event):
            if self.password.get()=="Password":
                self.password.delete(0, tk.END)
        def u_focusout(event):
            if self.user_name.get()=="":
                self.user_name.insert(0,"Username")
        def p_focusout(event):
            if self.password.get()=="":
                self.password.insert(0,"Password")
        def on_click():
            if self.var.get() == False:
                messagebox.showwarning("Login Failed","You must agree to the terms and conditions.")
            else:
                user_name = self.user_name.get()
                password = self.password.get()
                if not user_name or not password:
                    messagebox.showwarning("Login Failed","Please enter both username and password.")
                else:
                    messagebox.showinfo("Login Successful",f"Welcome, {user_name}!")


        self.background_image = tk.PhotoImage(file="C:\\Users\\Rafiullah\\Desktop\\back4.png")
        canvas = tk.Canvas(self,width=800, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0,0, image = self.background_image, anchor="nw")
        self.frame = tk.Frame(self, bg="light gray", bd=5, relief="ridge")
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=350)
        self.lable = tk.Label(self.frame, text="LOGIN", font=("Times New Roman",30),fg="black", background="light gray" )
        self.lable.pack(side="top", fill="both",padx=1, pady=20)
        
        self.user_name = tk.Entry(self.frame, width=200, font=("Times New Roman",16))
        self.user_name.pack(padx=20,pady=10)
        self.password = tk.Entry(self.frame, width=200, font=("Times New Roman",14))
        self.password.pack(padx=20,pady=15)
        self.user_name.insert(0,"Username")
        self.password.insert(0, "Password")
        self.user_name.bind("<FocusIn>", u_focusin)
        self.user_name.bind("<FocusOut>", u_focusout)
        self.password.bind("<FocusIn>", p_focusin)
        self.password.bind("<FocusOut>", p_focusout)
        
        
        self.var = tk.IntVar()
        self.checkbutton = tk.Checkbutton(self.frame, text="I agree to the terms and conditions", bg="light gray", variable=self.var, onvalue=True, offvalue=False)
        self.checkbutton.pack(pady=10)
        self.login_button = tk.Button(self.frame, text="LOGIN", bg="#7A4E2B",font=("Times New Roman", 12), bd=5, command=on_click)
        self.login_button.pack( side="left", padx=60, pady=5)
        self.logout = tk.Button(self.frame, text="LOGOUT", bg="#7A4E2B",font=("Times New Roman", 12), bd=5, command=quit) 
        self.logout.pack( side="left", padx=40, pady=5)
        self.mainloop()
    
# LoginApp()


# 35. Create a class WeatherApp that uses tkinter to create a weather information GUI.
# import required modules 
config_file = "config.ini"
config = ConfigParser() 
config.read(config_file) 
api_key = config['gfg']['api'] 
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def getweather(city): 
    result = requests.get(url.format(city, api_key)) 
      
    if result: 
        json = result.json() 
        city = json['name'] 
        country = json['sys'] 
        temp_kelvin = json['main']['temp'] 
        temp_celsius = temp_kelvin-273.15
        weather1 = json['weather'][0]['main'] 
        final = [city, country, temp_kelvin,  
                 temp_celsius, weather1] 
        return final 
    else: 
        print("NO Content Found") 
  
def search(): 
    city = city_text.get() 
    weather = getweather(city) 
    if weather: 
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1]) 
        temperature_label['text'] = str(weather[3])+"   Degree Celsius"
        weather_l['text'] = weather[4] 
    else: 
        messagebox.showerror('Error', "Cannot find {}".format(city)) 
app = tk.Tk() 
app.title("Weather App") 
app.geometry("300x300") 
city_text = tk.StringVar() 
city_entry = tk.Entry(app, textvariable=city_text) 
city_entry.pack() 
Search_btn = tk.Button(app, text="Search Weather",  
                    width=12, command=search) 
Search_btn.pack() 
location_lbl = tk.Label(app, text="Location", font={'bold', 20}) 
location_lbl.pack() 
temperature_label = tk.Label(app, text="") 
temperature_label.pack() 
weather_l = tk.Label(app, text="") 
weather_l.pack() 
# app.mainloop() 
