import typing
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from tkinter import messagebox
from H_3_menu_bar_of_homework import MenuOfHomework



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
                    if user_name.lower() == "rafiullah" and password == '001':
                        self.destroy()
                        MenuOfHomework()
                    else:
                        messagebox.showerror("Incorect Username or Password", "Your Username or Password is incorect") 
        self.background_image = tk.PhotoImage(file="background.png")
        # "C:\\Users\\Rafiullah\\Desktop\\back4.png"
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
        self.login_button.pack( side="left", padx=60, pady=20)
        self.logout = tk.Button(self.frame, text="LOGOUT", bg="#7A4E2B",font=("Times New Roman", 12), bd=5, command=quit) 
        self.logout.pack( side="left", padx=40, pady=10)
        self.mainloop()
    
LoginApp()