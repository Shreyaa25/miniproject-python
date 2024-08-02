import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image,ImageTk #pip install pillow

class Start:
    def __init__(self,root):
        self.root=root
        self.root.title("Start Page")
        self.root.geometry("1535x800+0+0")
        self.root.attributes('-fullscreen',True)
        self.root.config(bg="light blue")

        main_frame=Frame(self.root,relief=RIDGE,bg="white")
        main_frame.place(x=300,y=150,width=920,height=550)

        lbl_title=Label(self.root,text="Login As?",font=("times new roman",40,"bold"),bg="light yellow",fg="black",relief=RIDGE)
        lbl_title.place(x=300,y=75,width=920,height=75)

        title=Label(self.root,text="User Login",font=("times new roman",30,"bold"),fg="black",relief=RIDGE)
        title.place(x=400,y=600,width=250,height=50)

        title=Label(self.root,text="Admin Login",font=("times new roman",30,"bold"),fg="black",relief=RIDGE)
        title.place(x=870,y=600,width=250,height=50)

        login_btn = PhotoImage(file='images/user_login.png')
        admin_btn = PhotoImage(file='images/admin_login.png')

        btn_login=tk.Button(main_frame,image=login_btn,command=self.user_login)
        btn_login.place(x=100,y=150,width=250,height=250)
        btn_login.image=login_btn

        btn_admin_login=tk.Button(main_frame,image=admin_btn,command=self.admin_login)
        btn_admin_login.place(x=570,y=150,width=250,height=250)
        btn_admin_login.image=admin_btn

    def user_login(self):
        self.root.destroy()
        import login
        
    def admin_login(self):
        self.root.destroy()
        import admin

root=tk.Tk()
obj=Start(root)
root.mainloop()