from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2 


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Authentication Attendance  System")
        
        
        #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_parent=StringVar()
        
        
        
        #background image
        img3=Image.open(r"D:\face_recognition system\college_images\studentdetail.jpg")
        img3= img3.resize((1920, 1080), Image.BICUBIC)
        self.photoimage3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        title_lbl=Label(bg_img,text="Profile",font=("times new roman",40,"italic"),bg="tomato",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1920,height=60)
        
        main_frame=Frame(bg_img,bd=10,bg="white")
        main_frame.place(x=25,y=90,width=1820,height=950)
        
        # Left label frame
        
        Left_frame=LabelFrame(main_frame,bd=10,relief=RIDGE,text="Student Details",font=("pluto",35,"bold"),fg="teal")
        Left_frame.place(x=10,y=30,width=880,height=850)
        
        #Current Course
        Current_course_frame=LabelFrame(Left_frame,bd=10,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",18,"italic"))
        Current_course_frame.place(x=10,y=60,width=830,height=180)
        
        
        #Department
        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"italic"),state="readonly")
        dep_combo["values"]=("Select Department","Information Technology")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1 ,padx=2 ,pady=10,sticky=W)
        
        # Course
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",15,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",13,"italic"),state="readonly")
        course_combo["values"]=("Select Course","BSC.CSIT","BCA","BIT")
        course_combo.current(0)
        course_combo.grid(row=0,column=3 ,padx=2 ,pady=10,sticky=W)
        
        #Year
        year_label=Label(Current_course_frame,text="Year",font=("times new roman",15,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",13,"italic"),state="readonly")
        year_combo["values"]=("Select Year","2076","2077","2078")
        year_combo.current(0)
        year_combo.grid(row=1,column=1 ,padx=2 ,pady=10,sticky=W)
        
        
        #Semester
        semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",15,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"italic"),state="readonly")
        semester_combo["values"]=("Select Semester","III","IV","VII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3 ,padx=1 ,pady=10,sticky=W)
        
        
        #Class Student Information
        Class_student_frame=LabelFrame(Left_frame,bd=10,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",18,"italic"))
        Class_student_frame.place(x=10,y=320,width=830,height=450)
        
        #student Name
        studentName_label=Label(Class_student_frame,text="Student Name:",font=("times new roman",15,"bold"),bg="white")
        studentName_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentName_entry=ttk.Entry(Class_student_frame,width=18,textvariable=self.var_std_name,font=("times new roman",15,"italic"))
        studentName_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        
        #student ID
        studentID_label=Label(Class_student_frame,text="Student ID:",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(Class_student_frame,width=18,textvariable=self.var_std_id,font=("times new roman",15,"italic"))
        studentID_entry.grid(row=0,column=3,padx=0,sticky=W)
        
        
        #Section
        class_div_label=Label(Class_student_frame,text="Section:",font=("times new roman",15,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        
        
        
        div_combo=ttk.Combobox(Class_student_frame,width=12,textvariable=self.var_sec,font=("times new roman",16,""),state="readonly")
        div_combo["values"]=("Select Section","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1 ,padx=10 ,pady=5,sticky=W)
        
        #Rollno
        roll_no_label=Label(Class_student_frame,text="Roll No:",font=("times new roman",15,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(Class_student_frame,width=18,textvariable=self.var_roll,font=("times new roman",15,"italic"))
        roll_no_entry.grid(row=1,column=3,padx=0,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(Class_student_frame,text="Gender:",font=("times new roman",15,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
    
        
        gender_combo=ttk.Combobox(Class_student_frame,width=12,textvariable=self.var_gender,font=("times new roman",16,"italic"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Nonbinary")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1 ,padx=10 ,pady=5,sticky=W)
        
        #DOB
        dob_label=Label(Class_student_frame,text="DOB:",font=("times new roman",15,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(Class_student_frame,width=18,textvariable=self.var_dob,font=("times new roman",15,"italic"))
        dob_entry.grid(row=2,column=3,padx=0,pady=5,sticky=W)
        
        
        #EMAIL
        email_label=Label(Class_student_frame,text="Email:",font=("times new roman",15,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(Class_student_frame,width=18,textvariable=self.var_email,font=("times new roman",15,"italic"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        #Phone Number
        phone_label=Label(Class_student_frame,text="Phone No:",font=("times new roman",15,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(Class_student_frame,width=18,textvariable=self.var_phone,font=("times new roman",15,"italic"))
        phone_entry.grid(row=3,column=3,padx=0,pady=5,sticky=W)
        
        
        #Parent Name
        teacher_label=Label(Class_student_frame,text="Parent Name:",font=("times new roman",15,"bold"),bg="white")
        teacher_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(Class_student_frame,width=18,textvariable=self.var_parent,font=("times new roman",15,"italic"))
        teacher_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
        #Address
        address_label=Label(Class_student_frame,text="Address:",font=("times new roman",15,"bold"),bg="white")
        address_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(Class_student_frame,width=18,textvariable=self.var_address,font=("times new roman",15,"italic"))
        address_entry.grid(row=4,column=3,padx=0,pady=5,sticky=W)
        
        
        #Radio button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radiobutton1.grid(row=6,column=1,padx=4,pady=4,sticky=W)
        
        
        radiobutton2=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=6,column=2,padx=4,pady=4,sticky=W)
        
        #Buttons Frame
        btn_frame=Frame(Class_student_frame,bd=5,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=270,width=790,height=55)
        
        #save
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=12,font=("Arial",15,"bold"),bg="DodgerBlue",fg="white")
        save_btn.grid(row=0,column=0,padx=0 ,pady=0)
        
        
        #update
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=12,font=("Arial",15,"bold"),bg="dark green",fg="white")
        update_btn.grid(row=0,column=1,padx=4 ,pady=4)
        
        
        #Delete
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=12,font=("Arial",15,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2,padx=2 ,pady=2)
        
        #Reset
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("Arial",15,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3,padx=3 ,pady=1)
        
        
        #Buttons Frame1
        btn_frame1=Frame(Class_student_frame,bd=5,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=330,width=790,height=55)
        
        #Take Photo Sample
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=25,font=("Arial",15,"bold"),bg="DodgerBlue",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=2 ,pady=4)
        
        #update photo
        update_photo_btn=Button(btn_frame1,text="Update Photo",width=25,font=("Arial",15,"bold"),bg="DodgerBlue",fg="white")
        update_photo_btn.grid(row=0,column=1,padx=4 ,pady=1)
        
        
        # Right label frame
    
        Right_frame=LabelFrame(main_frame,bd=10,relief=RIDGE,text="Information",font=("pluto",35,"bold"),fg="teal")
        Right_frame.place(x=910,y=30,width=900,height=850)
        
        
        #Search 
        Search_frame=LabelFrame(Right_frame,bd=10,bg="white",relief=RIDGE,text="Search",font=("times new roman",30,"italic"))
        Search_frame.place(x=10,y=60,width=865,height=145)
        
        search_label=Label(Search_frame,text="Search By:",font=("times new roman",20,"bold"),bg="cyan",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        
        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_searchTX,font=("times new roman",18,"italic"),state="readonly",width=10)
        search_combo["values"]=("Select", "Roll_No","Phone_No","Student_ID")
        search_combo.grid(row=0,column=1 ,padx=5 ,pady=5,sticky=W)
        
        self.var_search=StringVar()
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_searchTX,width=14,font=("times new roman",15,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)
    
    
        search_btn=Button(Search_frame,command=self.search_data,text="Search",width=9,font=("Arial",15,"bold"),bg="cyan",fg="white")
        search_btn.grid(row=0,column=3,padx=5 ,pady=5)
        
        
        showAll_btn=Button(Search_frame,command=self.fetch_data,text="Show All",width=9,font=("Arial",15,"bold"),bg="cyan",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3 ,pady=4)
        
        
        #Table Frame
        table_frame=Frame(Right_frame,bd=10,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=220,width=865,height=550)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","roll","gender","sec","dob","email","phone","address","parent","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("parent",text="Parent")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=130)
        self.student_table.column("course",width=70)
        self.student_table.column("year",width=70)
        self.student_table.column("sem",width=80)
        self.student_table.column("id",width=80)
        self.student_table.column("name",width=130)
        self.student_table.column("roll",width=70)
        self.student_table.column("gender",width=70)
        self.student_table.column("sec",width=60)
        self.student_table.column("dob",width=95)
        self.student_table.column("email",width=170)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=120)
        self.student_table.column("parent",width=130)
        self.student_table.column("photo",width=150)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    
    #function declaration
    
    def add_data(self): 
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="": 
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@1230",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(), 
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_sec.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_parent.get(),
                                                                                                                self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been Added   Successfully",parent=self.root)      
            except Exception as es:
             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
            
    #FetCH Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@1230",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT *  from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()    
        conn.close()    
        
        
        #get Cursor
    def get_cursor(self,event=""):    
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            data=content["values"]
            
            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_std_id.set(data[4]),
            self.var_std_name.set(data[5]),
            self.var_roll.set(data[6]),
            self.var_gender.set(data[7]),
            self.var_sec.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_parent.set(data[13]),
            self.var_radio1.set(data[14]),
            
    #Update Function        
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="": 
            messagebox.showerror("Error","All Fields are required",parent=self.root) 
        else:
            try:
                Update=messagebox.askyesno("Update","Do You Want to Update this Student Details" ,parent=self.root)   
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@1230",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Sec=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Parent=%s,PhotoSample=%s WHERE Student_id=%s",(
                                                                                                                                                                                    
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_roll.get(), 
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_sec.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_parent.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_std_id.get()
                                                                                                                                                                                
                
                                                                                                                                                                                ))
                else:
                    if  not Update:
                            return
                messagebox.showinfo("Successully Updated","Student Details Successfully Update Completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}" ,parent=self.root)
            
                    
    #Delete Functions
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required to delete",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Profile Delete","Are you sure you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Test@1230",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()  
                messagebox.showinfo("Delete","Successfully Deleted Student Detail",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}" ,parent=self.root)                
                    
    #Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_sec.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_parent.set("")
        self.var_radio1.set("")
    
    #Search Data
    def search_data(self):
        
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@1230",database="face_recognizer")
                my_cursor=conn.cursor()
                sql="SELECT Student_id,Name,Department,Course,Year,Semester,Section,Gender,DOB,Phone,Address,Roll_No,Email,Parent,PhotoSample FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)     
        
        
        #Generate data set or Take Photo Samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="": 
            messagebox.showerror("Error","All Fields are required",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@1230",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT * from student")
                myResult=my_cursor.fetchall()
                id=0
                for x in myResult:
                    id+=1
                my_cursor.execute("UPDATE student SET Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Roll=%s,Gender=%s,Sec=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Parent=%s,PhotoSample=%s WHERE Student_id=%s",(
                                                                                                                                                                                    
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_sec.get(), 
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_parent.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                                
                
                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                
                    #Load Open CV      
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    
                    
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0) 
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}" ,parent=self.root)    
                    
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()        