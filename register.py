from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

import tkinter as tk
from tkinter import messagebox
import mysql.connector


root = tk.Tk()
root.title("Register")

#variable:

var_fname=StringVar()
var_lname=StringVar()
var_contact=StringVar()
var_email=StringVar()
var_securityQ=StringVar()
var_securityA=StringVar()
var_pass=StringVar()
var_confpass=StringVar()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


image = Image.open("D:\\python1\\Hotel_Management_System\\images\\download7.jpg")
image = image.resize((screen_width, screen_height), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)


canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, anchor="nw", image=background_image)

# img1 = Image.open("D:\\python1\\Hotel_Management_System\\ima
# ges\\bac1.jpg")
# img1 = img1.resize((100, 100), Image.ANTIALIAS)
# photoimage1 = ImageTk.PhotoImage(img1)


# lblimg1 = Label(image=photoimage1)
# lblimg1.place(x=50, y=100,width=470,height=550)
bg1=ImageTk.PhotoImage(file="D:\\python1\\Hotel_Management_System\\images\\reg2.png")
left_lbl=Label(root,image=bg1)
left_lbl.place(x=50,y=100,width=490,height=550)


frame=Frame(root,bg="white")
frame.place(x=540,y=100,width=800,height=550)

register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
register_lbl.place(x=20,y=20)

fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
fname.place(x=50,y=100)

fname_entry=ttk.Entry(frame,textvariable=var_fname,font=("times new roman",15,"bold"))
fname_entry.place(x=50,y=130,width=250)

l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
l_name.place(x=370,y=100)

txt_lname=ttk.Entry(frame,textvariable=var_lname,font=("times new roman",15))
txt_lname.place(x=370,y=130,width=250)


contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
contact.place(x=50,y=170)

txt_contact=ttk.Entry(frame,textvariable=var_contact,font=("times new roman",15))
txt_contact.place(x=50,y=200,width=250)

email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
email.place(x=370,y=170)

txt_email=ttk.Entry(frame,textvariable=var_email,font=("times new roman",15))
txt_email.place(x=370,y=200,width=250)

security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
security_Q.place(x=50,y=240)

combo_security_Q=ttk.Combobox(frame,textvariable=var_securityQ,font=("times new roman",15,"bold"),state="readonly")
combo_security_Q["values"]=("Select","What was the first concert you attended?","What city were you born in?","What was the make and model of your first car?")
combo_security_Q.place(x=50,y=270,width=250)
combo_security_Q.current(0)

security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
security_A.place(x=370,y=240)

txt_security=ttk.Entry(frame,textvariable=var_securityA,font=("times new roman",15))
txt_security.place(x=370,y=270,width=250)

pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
pswd.place(x=50,y=310)

txt_pswd=ttk.Entry(frame,textvariable=var_pass,font=("times new roman",15))
txt_pswd.place(x=50,y=340,width=250)

confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
confirm_pswd.place(x=370,y=310)

txt_confirm_pswd=ttk.Entry(frame,textvariable=var_confpass,font=("times new roman",15))
txt_confirm_pswd.place(x=370,y=340,width=250)

var_check=IntVar()
checkbtn=Checkbutton(frame,variable=var_check,text="I agree the Terms & Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
checkbtn.place(x=50,y=380)

img = Image.open("D:\\python1\\Hotel_Management_System\\images\\reg8.jfif")
img=img.resize((200,55),Image.ANTIALIAS)
photoimage=ImageTk.PhotoImage(img)
b1=Button(frame,image=photoimage,command=lambda:register_data(),borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
b1.place(x=10,y=420,width=200)

img1 = Image.open("D:\\python1\\Hotel_Management_System\\images\\loginnow5.jfif")
img1=img1.resize((200,45),Image.ANTIALIAS)
photoimage1=ImageTk.PhotoImage(img1)
b1=Button(frame,image=photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
b1.place(x=330,y=420,width=200)

# functionality for registeration page:

def register_data():
    if var_fname.get() == "" or var_email.get() == "" or var_securityQ.get() == "Select":
        messagebox.showerror("Error", "All fields are required")
    elif var_pass.get() != var_confpass.get():
        messagebox.showerror("Error", "Password & Confirm Password must be the same")
    elif var_check.get() == 0:
        messagebox.showerror("Error", "Please agree to our Terms and Conditions")
    else:
        conn = mysql.connector.connect(host="localhost", user="root",password="07121999", database="hotelm")
        my_cursor = conn.cursor()
        query = ("select * from register where email = %s")
        value = (var_email.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()
        if row != None:
            messagebox.showerror("Error", "User already exists. Please try another email.")
        else:
            my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    var_fname.get(),
                                                                                    var_lname.get(),
                                                                                    var_contact.get(),
                                                                                    var_email.get(),
                                                                                    var_securityQ.get(),
                                                                                    var_securityA.get(),
                                                                                    var_pass.get()
            
                                                                                    ))
            
            # my_cursor.execute(insert_query, insert_values)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")

