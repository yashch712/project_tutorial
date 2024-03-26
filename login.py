rom tkinter import *
from tkinter import ttk,Toplevel,Button
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


def main():
    # win=Tk()
    # app=win
    # win.mainloop()
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
    lblimg1.place(x=730, y=170, width=100, height=100)

    get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
    get_str.place(x=95, y=100)

    username = lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
    username.place(x=70, y=155)

    txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
    txtuser.place(x=40, y=180, width=270)

    password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
    password.place(x=70, y=225)

    txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
    txtpass.place(x=40, y=250, width=270)

    img2 = Image.open("D:\\python1\\Hotel_Management_System\\images\\icon.png")
    img2 = img2.resize((25, 25), Image.ANTIALIAS)
    photoimage2 = ImageTk.PhotoImage(img2)

    lblimg1 = Label(image=photoimage2, bg="black", borderwidth=0)
    lblimg1.place(x=650, y=323, width=25, height=25)

    img3 = Image.open("D:\\python1\\Hotel_Management_System\\images\\password5.jfif")
    img3 = img3.resize((25, 25), Image.ANTIALIAS)
    photoimage3 = ImageTk.PhotoImage(img3)

    lblimg1 = Label(image=photoimage3, bg="black", borderwidth=0)
    lblimg1.place(x=650, y=393, width=25, height=25)

    loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white",
                      bg="red", command=lambda: login())
    loginbtn.place(x=110, y=300, width=120, height=35)

    registerbtn = Button(frame, text="New User Register",command=lambda:register_window(), font=("times new roman", 10, "bold"), borderwidth=0,
                         fg="white", bg="black", activeforeground="white", activebackground="black")
    registerbtn.place(x=15, y=350, width=160)

    registerbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0,
                         fg="white", bg="black", activeforeground="white", activebackground="black")
    registerbtn.place(x=10, y=370, width=160)

    # root.mainloop()
    
    def register_window():
        new_window = Toplevel(root)
        app=new_window
     
    # def open_register_window():
    #     register_window(frame)
        
    # frame.mainloop()
    

    root.mainloop()
    def login():
        if txtuser.get() == "" or txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required.")
        elif txtuser.get() == "yess" and txtpass.get() == "yash":
            messagebox.showinfo("Success", "Login successful!")
        else:
            conn = mysql.connector.connect(host="localhost", user="root",password="07121999", database="hotelm")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    var_email.get(),
                                                                                    var_pass.get()
                                                                            ))
            
            row =my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error,invalid username or password")
            else:
                open_main=messagebox.askyesno("YesNo,Access only admin")
                if open_main>0:
                    new_window=Toplevel(new_window)
                    # app=Hospital(new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
# register.py          
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
    


if __name__ == "__main__":
    main()
