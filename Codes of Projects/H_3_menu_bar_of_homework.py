from typing import Any
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from demo import extract
import os


built_in_file = open("H_1_built_in_fanctions.py")
text_of_built_in_fanction = list(built_in_file.readlines())
recursive_file = open("H_2_Examples_of_Recursive.py")
text_of_recursive_file = list(recursive_file.readlines())
menubar_file = open("H_3_menu_bar_of_homework.py")
text_of_menubar = list(menubar_file.readlines())
oop_file = open ("H_4_OOP_Homework.py")
text_of_OOP = list(oop_file.readlines())


class MenuOfHomework(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Home works")
        self.geometry("600x440+100+100")
        self.resizable(False,False)
        self.menubar = Menu(self)
        self.menu_frame = tk.Frame(self, bg="#f0f0f0")
        self.menu_frame.pack(side="top",fill=tk.X)
        self.frame2 = tk.Frame(self, bg="#f0f0f0")
        self.frame2.pack(side="top",fill=tk.X, pady=20)
        self.frame2.columnconfigure((1,2,3), weight=1)
        self.frame2.rowconfigure((0,1,2), weight=1)
        self.label0 = ttk.Label(self.frame2, text="Kabul University", font=("Times New Roman", 16))
        self.label0.grid(row=0, column=2, padx=10)
        self.label0 = ttk.Label(self.frame2, text="Computer Scince Faculty", font=("Times New Roman", 16))
        self.label0.grid(row=2, column=2, padx=10)
        self.label0 = ttk.Label(self.frame2, text="Department of Sofeware Engineering", font=("Times New Roman", 16))
        self.label0.grid(row=3, column=2, padx=10)
        self.label = ttk.Label(self.frame2, text="Tkinter and OOP Project", font=("Modern No. 20", 38, "bold"))
        self.label.grid(row=4, column=2, padx=10, pady=70)
        self.label1 = ttk.Label(self.frame2, text="     Prepared by: Rafiullah Abid\n     Teacher: Ahmad Roheed khaliqyar", font=("Times New Roman",16))
        self.label1.grid(row=5, column=1, columnspan=2, sticky="sw", pady=5)
        
        def homework1():
            self.destroy()
            def close():
                self.window1.destroy()
                MenuOfHomework()
            self.window1= tk.Tk()
            self.window1.geometry("600x470+100+100")
            self.window1.title("Built-in Fanctions")
            self.window1.frame= tk.Frame(self.window1)
            self.window1.frame.pack()
            self.window1.built = tk.Label(self.window1.frame, text="Python Built in Fanctions",font=("Times New Roman",18,"bold"))
            self.window1.built.pack()
            self.window1.text = tk.Text(self.window1)
            self.window1.text.insert(tk.END,text_of_built_in_fanction)
            self.window1.text.pack(side="top",expand=True, fill="both")
            self.window1.scrollbar = tk.Scrollbar(self.window1.text)
            self.window1.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
            self.window1.text.config(yscrollcommand=self.window1.scrollbar.set)
            self.window1.scrollbar.config(command=self.window1.text.yview)
            self.button = tk.Button(self.window1, text="Home", command=close, bg="#7A4E2B", bd=5)
            self.button.pack()
            self.window1.mainloop()
        
        def homework2():
            self.destroy()
            def close():
                self.window2.destroy()
                MenuOfHomework()
            self.window2= tk.Tk()
            self.window2.geometry("600x470+100+100")
            self.window2.title("Recursive Fanctions")
            self.window2.frame= tk.Frame(self.window2)
            self.window2.frame.pack()
            self.window2.recursive = tk.Label(self.window2.frame, text="Python Recursive Fanctions",font=("Times New Roman",18,"bold"))
            self.window2.recursive.pack()
            self.window2.text = tk.Text(self.window2)
            self.window2.text.insert(tk.END,text_of_recursive_file)
            self.window2.text.pack(side="top",expand=True, fill="both")
            self.button = tk.Button(self.window2, text="Home", command=close, bg="#7A4E2B", bd=5)
            self.button.pack()
            self.window2.mainloop()
        
        def homework3():
            self.destroy()
            def close():
                self.window3.destroy()
                MenuOfHomework()
            self.window3= tk.Tk()
            self.window3.geometry("600x470+100+100")
            self.window3.title("Menubar Codes")
            self.window3.frame= tk.Frame(self.window3)
            self.window3.frame.pack()
            self.window3.built = tk.Label(self.window3.frame, text="Menubar Project Codes",font=("Times New Roman",18,"bold"))
            self.window3.built.pack()
            self.window3.text = tk.Text(self.window3)
            self.window3.text.insert(tk.END,text_of_menubar)
            self.window3.text.pack(side="top",expand=True, fill="both")
            self.window3.scrollbar = tk.Scrollbar(self.window3.text)
            self.window3.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
            self.window3.text.config(yscrollcommand=self.window3.scrollbar.set)
            self.window3.scrollbar.config(command=self.window3.text.yview)
            self.button = tk.Button(self.window3, text="Home", command=close, bg="#7A4E2B", bd=5)
            self.button.pack()
            self.window3.mainloop()
        def open_folder():
            folder_path = "E:\\OOP homework\\OOP_Folder"
            os.startfile(folder_path)
            self.folder_window.destroy()

        def extract_files():
            extract()
            self.folder_window = tk.Tk()
            self.folder_window.geometry("300x200+200+200")
            self.folder_window.title("Generating The files")
            self.folder_window.label = tk.Label(self.folder_window, text="The files generated in OOP_Folder", font=("Times New Roman", 14))
            self.folder_window.label.pack(pady=50)
            self.folder_window.button = tk.Button(self.folder_window, text="Open folder",command=open_folder, background="light gray")
            self.folder_window.button.pack()
            self.window4.button_oop.config(state = "disable")
        def homework4():
            self.destroy()
            def close():
                self.window4.destroy()
                MenuOfHomework()
            self.window4= tk.Tk()
            self.window4.geometry("600x440+100+100")
            self.window4.title("OOP And Tkinter Project")
            self.window4.frame= tk.Frame(self.window4)
            self.window4.frame.pack()
            self.window4.oop = tk.Label(self.window4.frame, text="35 Question of OOP and Tkinter",font=("Times New Roman",18,"bold"))
            self.window4.oop.pack()
            self.window4.oop_ex = tk.Label(self.window4.frame, text="if you want to run each of these question click",font=("Times New Roman",14,"bold"))
            self.window4.oop_ex.pack(side="left",pady=10)
            self.window4.button_oop = tk.Button(self.window4.frame, text="here",command=extract_files, fg="blue", bd=0,font=("Times New Roman",14))
            self.window4.button_oop.pack(side="left")
            self.window4.text = tk.Text(self.window4, bg="#ffffff", fg="#000000")
            self.window4.text.insert(tk.END, text_of_OOP)
            self.window4.text.pack(side="top",padx=10, expand=True, fill="both")
            self.window4.scrollbar = tk.Scrollbar(self.window4.text)
            self.window4.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
            self.window4.text.config(yscrollcommand=self.window4.scrollbar.set)
            self.window4.scrollbar.config(command=self.window4.text.yview)
            self.button = tk.Button(self.window4, text="Home", command=close, bg="#7A4E2B", bd=5)
            self.button.pack()

            self.window4.mainloop()
        
        def add_menu_item(frame, text, command):
            def on_enter(event):
                button["background"] = "lightblue"
            def on_leave(event):
                button["background"]= "#ffffff"
            button = tk.Button(frame, text=text, command=command, 
                       bg="#ffffff", fg="#000000", padx=20, pady=10, bd=0, 
                       activebackground="#e0e0e0", font=("Helvetica", 12, "bold"))
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
            button.pack(side=tk.LEFT, padx=5, pady=5)
            

        add_menu_item(self.menu_frame, "Homework 1", homework1)
        add_menu_item(self.menu_frame, "Homework 2", homework2)
        add_menu_item(self.menu_frame, "Homework 3", homework3)
        add_menu_item(self.menu_frame, "Homework 4", homework4)

        self.mainloop()
MenuOfHomework()



