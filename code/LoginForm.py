from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql #pip install pymysql

# pip install pillow


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("900x600+100+100")
        self.root.resizable(False, False) #important 

        # Background Image
        self.bg=ImageTk.PhotoImage(file="c:/Users/GG2Admin/Documents/Refference Code/1.Python/1.Zelda Python Game/code/login_regi/login01.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login Frame
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=100, y=100, width=500, height=400)

        # Title & SubTitle
        title = Label(login_frame, text="Login Here", font=("impact", 28, "bold"), fg="green", bg="white").place(x=90, y=20)
        subtitle = Label(login_frame, text="Player Login", font=("Goudy old style", 15, "bold"), bg="white").place(x=90, y=70)

        # Email
        email = Label(login_frame, text="Enter Your Email", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=100)
        self.txt_email = Entry(login_frame, font=("Goudy old style", 15), bg="white")
        self.txt_email.place(x=90, y=130, width=320, height=35)

        # Password
        lbl_password = Label(login_frame, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=170)
        self.password = Entry(login_frame, font=("Goudy old style", 15), bg="white")
        self.password.place(x=90, y=200, width=320, height=35)

        # Buttons
        btn_forgot = Button(login_frame, text="Forgot Password ?", bd=0, cursor="hand2", font=("Goudy old style", 13, "bold"), fg="red", bg="white").place(x=90, y=240)
        btn_login = Button(login_frame, command=self.login, cursor="hand2", text="Login", bd=0, font=("Goudy old style", 13, "bold"), fg="white", bg="green").place(x=90, y=280)
        
        btn_reg=Button(login_frame,text="Register New Account",command=self.register_window,font=("time new roman",13,"bold"),fg="white",bd=0,bg="green", cursor="hand2").place(x=90, y=330)
        
    def register_window(self):
        self.root.destroy()
        import RegisterForm
                        
    def login(self):
        if self.txt_email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="zelda_python_game")
                cur=con.cursor()
                cur.execute("select * from player where email=%s and password=%s",(self.txt_email.get(),self.password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Welcome Gamer", parent=self.root)
                con.close()                               
                
                
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=self.root)
            
        

root = Tk()
obj = Login(root)
root.mainloop()
