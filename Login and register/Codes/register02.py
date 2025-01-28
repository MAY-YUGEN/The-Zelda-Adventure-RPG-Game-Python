from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Register:
    def __init__(self,root):
        self.root = root 
        self.root.title("Registeration Form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        
        # BG Image
        self.bg=ImageTk.PhotoImage(file="Codes/All Images/2.png")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        # Left Image
        self.left=ImageTk.PhotoImage(file="Codes/All Images/1.png")
        LEFT=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        
        
        # Register Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title=Label(frame1,text="Register Here",font=("time new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        
        #-----------Row1
        f_name=Label(frame1,text="First Name",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("time new roman",15),bg="lightgray").place(x=50,y=130,width=250) 
        
        l_name=Label(frame1,text="Last Name",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        txt_fname=Entry(frame1,font=("time new roman",15),bg="lightgray").place(x=370,y=130,width=250) 
        
        #-----------Row2        
        contact=Label(frame1,text="Contact No.",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        txt_fname=Entry(frame1,font=("time new roman",15),bg="lightgray").place(x=50,y=200,width=250) 
        
        email=Label(frame1,text="E-Mail",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        txt_fname=Entry(frame1,font=("time new roman",15),bg="lightgray").place(x=370,y=200,width=250) 
        
        #-----------Row3        
        question=Label(frame1,text="Security Question",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        
        cmd_quest=ttk.Combobox(frame1,font=("time new roman",13),state='readonly',justify=CENTER) 
        cmd_quest['value']=("Select","Your Favorite Game Name","Your favorite Game Player")
        cmd_quest.place(x=50,y=270,width=250)
        cmd_quest.current(0)
        
        Answer=Label(frame1,text="Answer",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        txt_fname=Entry(frame1,font=("time new roman",15),bg="lightgray").place(x=370,y=270,width=250)
        
        #-----------Row4        
        password=Label(frame1,text="Password",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        txt_fname=Entry(frame1,font=("time new roman",15),bg="lightgray").place(x=50,y=340,width=250) 
        
        cpasword=Label(frame1,text="Conform Password",font=("time new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        txt_fname=Entry(frame1,font=("time new roman",15),bg="lightgray").place(x=370,y=340,width=250) 
        
        #-----Terms-----
        chk = Checkbutton(frame1,text="I Agreed the Terms & Conditions", onvalue=1, offvalue=0,bg="white",font=("time new roman",11),cursor="hand2").place(x=50,y=380)
        
        # Register button
        
        self.btn_img=ImageTk.PhotoImage(file="Codes/All Images/3.png")
        btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2").place(x=50,y=420)
        
        # Login Button
        btn_login=Button(self.root,text="Sign In", font=("time new roman",20),bd=0,cursor="hand2").place(x=200,y=500,width=180)         
           
root = Tk()
obj = Register(root)
root.mainloop()