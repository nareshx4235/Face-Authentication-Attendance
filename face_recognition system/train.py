from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl= Label(self.root, text = "TRAIN DATA SET", font= ("times new roman",33, "bold"),bg = "olive", fg="red")
        title_lbl.place(x=0, y=0, width= 1920, height= 50)
        
        img_top = Image.open(r"college_images\datafunnel2.jpg")
        img_top= img_top.resize((1920,500),Image.BICUBIC)
        self.photoimg_top = ImageTk.PhotoImage(img_top)   

        f_lbl= Label(self.root, image=  self.photoimg_top)
        f_lbl.place(x=0, y=45, width= 1920, height= 500)
        
        update_btn1= Button(self.root, text="TRAIN DATA",command=self.train_classifier, font=("rockwell",25,"bold"), bg= "cyan", fg="white")
        update_btn1.place(x=0,y=345,width=1920, height=60)
        
        img_bottom = Image.open(r"college_images\datafunnel.jpg")
        img_bottom= img_bottom.resize((1920,600),Image.BICUBIC)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)   
        

        f_lbl= Label(self.root, image=  self.photoimg_bottom)
        f_lbl.place(x=0, y=400, width= 1920, height= 600)
        
    def train_classifier(self):
        data_dir= ("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]   
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert("L") #grayscale image
            imageNp= np.array(img,'uint8')
            id= int(os.path.split(image)[1].split('.')[1])
            
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
                #********train the classifier and save******
        
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed") 
        
        
        
      
            
            
        



if __name__== "__main__":
    root= Tk()
    obj= Train(root) 
    root.mainloop()         
        