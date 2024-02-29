from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Login")




screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


image = Image.open("D:\\python1\\Hotel_Management_System\\images\\images (41).jpeg")
image = image.resize((screen_width, screen_height), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)


canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, anchor="nw", image=background_image)





frame = Frame(root, bg="black")
frame.place(x=610, y=170, width=340, height=450)

img1 = Image.open("D:\\python1\\Hotel_Management_System\\images\\icon.png")
img1 = img1.resize((100, 100), Image.ANTIALIAS)
photoimage1 = ImageTk.PhotoImage(img1)


lblimg1 = Label(image=photoimage1, bg="black", borderwidth=0)
lblimg1.place(x=730, y=170,width=100,height=100)
        
get_str = Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
get_str.place(x=95,y=100)

username=lbl= Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
username.place(x=70,y=155)

txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
txtuser.place(x=40,y=180,width=270)

password=lbl= Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
password.place(x=70,y=225)

txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
txtpass.place(x=40,y=250,width=270)


img2 = Image.open("D:\\python1\\Hotel_Management_System\\images\\icon.png")
img2 = img2.resize((25, 25), Image.ANTIALIAS)
photoimage2 = ImageTk.PhotoImage(img2)


lblimg1 = Label(image=photoimage2, bg="black", borderwidth=0)
lblimg1.place(x=650, y=323,width=25,height=25)

img3 = Image.open("D:\\python1\\Hotel_Management_System\\images\\password5.jfif")
img3 = img3.resize((25, 25), Image.ANTIALIAS)
photoimage3 = ImageTk.PhotoImage(img3)


lblimg1 = Label(image=photoimage3, bg="black",borderwidth=0)
lblimg1.place(x=650, y=393,width=25,height=25)

loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red",command=lambda:login())
loginbtn.place(x=110, y=300, width=120, height=35)


registerbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
registerbtn.place(x=15,y=350,width=160)


registerbtn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
registerbtn.place(x=10,y=370,width=160)

def login():
    if txtuser.get() == "" or txtpass.get() == "":
        messagebox.showerror("Error", "All fields are required.")
    elif txtuser.get() == "yess" and txtpass.get() == "yash":
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Invalid", "Invalid username or password.")
    
    
    


root.mainloop()
    





    
    