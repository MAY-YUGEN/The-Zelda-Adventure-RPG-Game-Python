from tkinter import *
from PIL import Image,ImageTk


class Register:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1350x700+0+0")
        
        # BG Image
        #C:\Users\GG2Admin\Documents\Refference Code\1.Python\1.Zelda Python Game\code\login_regi
        self.bg=ImageTk.PhotoImage(file="c:/Users/GG2Admin/Documents/Refference Code/1.Python/1.Zelda Python Game/code/login_regi/login01.png")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        
        
root=Tk()
obj=Register(root)
root.mainloop()
        



root.mainloop()