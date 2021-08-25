from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        # All Images
        self.bg_icon = ImageTk.PhotoImage(file="bg.png")
        self.user_icon = ImageTk.PhotoImage(file="user.png")
        self.lock_icon = ImageTk.PhotoImage(file="lock.png")
        self.logo_icon = ImageTk.PhotoImage(file='logo.png')

        # variables

        self.uname = StringVar()
        self.pass_ = StringVar()

        
        # Background
        bg_lbl = Label(self.root,image=self.bg_icon).pack()

        # title
        title = Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg='yellow',fg='red',bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        # Login Frame
        Login_frame = Frame(self.root,bg='white')
        Login_frame.place(x=400,y=150)
        
        ### Logo
        logolbl = Label(Login_frame,image=self.logo_icon,bg='white')
        logolbl.grid(row=0,pady=20,columnspan=2)
        
        ### Username
        lbluser = Label(Login_frame,text=' Username',image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
        lbluser.grid(row=1,column=0,padx=20,pady=10)
        txtuser = Entry(Login_frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE,textvariable=self.uname)
        txtuser.grid(row=1,column=1,padx=20)
        
        ### Password 
        lblpass = Label(Login_frame,text=' Password',image=self.lock_icon,compound=LEFT,font=("times new roman",20,"bold"),bg='white')
        lblpass.grid(row=2,column=0,padx=20,pady=10)
        txtpass = Entry(Login_frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE,textvariable=self.pass_)
        txtpass.grid(row=2,column=1,padx=20)
        
        ### Buttons
        btnlogin = Button(Login_frame,text='Login',font=("times new roman",20,"bold"),bg='yellow',fg='red',width=10,command=self.login)
        btnlogin.grid(row=3,column=1,pady=10)

    def login(self):
        if self.uname.get()=='' or self.pass_.get()=='':
            messagebox.showerror('Error','All fields are required!!')
        elif self.uname.get()=='Username' and self.pass_.get()=='Password':
            messagebox.showerror('Login Successfull','Welcome!')
        else:
            messagebox.showerror('Error','Invalid Username or Password')

                  
root = Tk()
obj = Login_System(root)
root.mainloop()