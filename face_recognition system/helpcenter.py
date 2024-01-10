from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpcenter:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

 
    



        # backgorund image 
        bg1=Image.open(r"D:\face_recognition system\college_images\bg4.png")
        bg1=bg1.resize((1920,1080),Image.BICUBIC)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1920,height=1080)


        #title section
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1920,height=50)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # LinkedIn Profile BUTTON
        std_img_btn=Image.open(r"D:\face_recognition system\college_images\linkedin_icon.png")
        std_img_btn=std_img_btn.resize((180,180),Image.BICUBIC)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.linkedLn,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.linkedLn,text="LinkedIn",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=250,y=380,width=180,height=45)

        # Facebook
        det_img_btn=Image.open(r"D:\face_recognition system\college_images\facebook logo_icon.png")
        det_img_btn=det_img_btn.resize((180,180),Image.BICUBIC)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=480,y=380,width=180,height=45)

         # Youtube
        att_img_btn=Image.open(r"D:\face_recognition system\college_images\yt.png")
        att_img_btn=att_img_btn.resize((180,180),Image.BICUBIC)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=710,y=380,width=180,height=45)

         # Gmail
        hlp_img_btn=Image.open(r"D:\face_recognition system\college_images\gmail_icon.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.BICUBIC)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=940,y=380,width=180,height=45)


        # create function for button 
    
    
    def linkedLn(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/nareshx4235/"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/naresh4235"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/channel/UCk7y7AYt0k2EKH1vsuDv8RA"
        webbrowser.open(self.url,new=self.new)
    
    
        
    
    def gmail(self):
        self.new = 1
        email_address = "nareshx4235@gmail.com"
        self.url = "https://www.gmail.com"
        subject = "Contact Me"
        mailto_url = f"mailto:{email_address}?subject={subject}"

        webbrowser.open(self.url,new=self.new)
        
    def run(self):
        self.window.mainloop()    






if __name__ == "__main__":
    root=Tk()
    obj=Helpcenter(root)
    root.mainloop()