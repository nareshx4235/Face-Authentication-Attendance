from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        
        

        # backgorund image 
        bg1=Image.open(r"D:\face_recognition system\college_images\bg4.png")
        bg1=bg1.resize((1920,1080),Image.BICUBIC)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1920,height=1000)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1920,height=60)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"D:\face_recognition system\college_images\naresh.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.BICUBIC)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,text="Naresh Adhikari",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=250,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\face_recognition system\college_images\yogesh.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.BICUBIC)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=500,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,text="Yogesh Bhattarai",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=500,y=380,width=210,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"D:\face_recognition system\college_images\basan.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.BICUBIC)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=750,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,text="Basan Ghimire",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=750,y=380,width=180,height=45)

         



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()