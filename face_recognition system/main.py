from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from helpcenter import Helpcenter




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
        
        b1=Button(bg_img,image=self.photoimage5,command=self.face_rec,cursor="hand2")
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
        os.startfile("data")
    
        
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
            obj=Face_Recognition_System(root)
            root.mainloop()