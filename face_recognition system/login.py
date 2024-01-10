from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
# --------------------------
from train import Train
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpcenter import Helpcenter
import os


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"D:\face_recognition system\college_images\loginBg1.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"D:\face_recognition system\college_images\log1.png")
        img1=img1.resize((100,100),Image.BICUBIC)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

        #label1 
        email =lb1= Label(frame1,text="Email:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        email.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,show="*",font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=90,y=370,width=50,height=20)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username="root", password="Test@1230",host="localhost",database="face_recognizer")
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face dection system====================
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Authentication Attendance  System")
        
        #FIRST IMAGE
        img=Image.open(r"D:\face_recognition system\college_images\right.png")
        img = img.resize((600, 150), Image.BICUBIC)
        self.photoimage=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=600,height=150)
        
        #second IMAGE
        img1=Image.open(r"D:\face_recognition system\college_images\aa.png")
        img1 = img1.resize((600, 150), Image.BICUBIC)
        self.photoimage1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=500,y=0,width=600,height=150)
        
        #Third image
        img2=Image.open(r"D:\face_recognition system\college_images\left.png")
        img2= img2.resize((1280, 150), Image.BICUBIC)
        self.photoimage2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=1100,y=0,width=1280,height=150)
        
        #background image
        img3=Image.open(r"D:\face_recognition system\college_images\faceback.PNG")
        img3= img3.resize((1920, 1080), Image.BICUBIC)
        self.photoimage3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=150,width=1920,height=1080)

        title_lbl=Label(bg_img,text="Face Authentication Attendance System",font=("times new roman",40,"bold"),bg="yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1920,height=60)
        
        #student profile Button
        img4=Image.open(r"D:\face_recognition system\college_images\profile.jpg")
        img4= img4.resize((220, 220), Image.BICUBIC)
        self.photoimage4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimage4,command=self.student_details,cursor="hand2")
        b1.place(x=350,y=150,width=220,height=220)
        
        b1=Button(bg_img,text="Profile",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="white") 
        b1.place(x=350,y=350,width=220,height=40)
        
        #Detect Face Button
        img5=Image.open(r"D:\face_recognition system\college_images\facedetector.PNG")
        img5= img5.resize((220, 220), Image.BICUBIC)
        self.photoimage5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimage5,cursor="hand2")
        b1.place(x=650,y=150,width=220,height=220)
        
        b1=Button(bg_img,text="Face Detector",command=self.face_rec,cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="white") 
        b1.place(x=650,y=350,width=220,height=40)
        
        #Attendance Button
        img6=Image.open(r"D:\face_recognition system\college_images\attendance.png")
        img6= img6.resize((220, 220), Image.BICUBIC)
        self.photoimage6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,command=self.attendance_pannel,image=self.photoimage6,cursor="hand2")
        b1.place(x=950,y=150,width=220,height=220)
        
        b1=Button(bg_img,text="Attendance",command=self.attendance_pannel,cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="white") 
        b1.place(x=950,y=350,width=220,height=40)
        
        
        #Help Center Button
        img7=Image.open(r"D:\face_recognition system\college_images\helpcenter.png")
        img7= img7.resize((220, 220), Image.BICUBIC)
        self.photoimage7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,command=self.helpSupport,image=self.photoimage7,cursor="hand2")
        b1.place(x=1250,y=150,width=220,height=220)
        
        b1=Button(bg_img,text="Help Center",command=self.helpSupport,cursor="hand2",font=("times new roman",20,"bold"),bg="cyan",fg="white") 
        b1.place(x=1250,y=350,width=220,height=40)
        
        #Train Data Button
        img8=Image.open(r"D:\face_recognition system\college_images\traindata.png")
        img8= img8.resize((220, 220), Image.BICUBIC)
        self.photoimage8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,command=self.train_pannels,image=self.photoimage8,cursor="hand2")
        b1.place(x=350,y=450,width=220,height=220)
        
        b1=Button(bg_img,text="Train Data",command=self.train_pannels,cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="white") 
        b1.place(x=350,y=650 ,width=220,height=40)
        
        
        #Photos Button
        img9=Image.open(r"D:\face_recognition system\college_images\photos.png")
        img9= img9.resize((220, 220), Image.BICUBIC)
        self.photoimage9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,command=self.open_img,image=self.photoimage9,cursor="hand2")
        b1.place(x=650,y=450,width=220,height=220)
        
        b1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="white") 
        b1.place(x=650,y=650 ,width=220,height=40)
        
        # About Us Button
        img10=Image.open(r"D:\face_recognition system\college_images\aboutus.jpg")
        img10= img10.resize((220, 220), Image.BICUBIC)
        self.photoimage10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,command=self.developer,image=self.photoimage10,cursor="hand2")
        b1.place(x=950,y=450,width=220,height=220)
        
        b1=Button(bg_img,text="About Us",command=self.developer,cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="white") 
        b1.place(x=950,y=650 ,width=220,height=40)
        
        #Log out Button
        img11=Image.open(r"D:\face_recognition system\college_images\logout.png")
        img11= img11.resize((220, 220), Image.BICUBIC)
        self.photoimage11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,command=self.Close,image=self.photoimage11,cursor="hand2")
        b1.place(x=1250,y=450,width=220,height=220)
        
        b1=Button(bg_img,command=self.Close,text="Log Out",cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="red") 
        b1.place(x=1250,y=650 ,width=220,height=40)
        
        
        #Function Buttons
    def open_img(self):
        os.startfile("dataset")
    
        
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)
            
    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpcenter(self.new_window)

    def Close(self):
        root.destroy()        
        
        
        
        
        
        
        
        
            
if __name__ == "__main__":
            root=Tk()
            app=Login(root)
            root.mainloop()
