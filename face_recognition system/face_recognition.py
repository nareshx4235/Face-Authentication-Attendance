from tkinter import*
from sys import path
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
import mysql.connector
import cv2
import os
import numpy as np
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION ", font=("verdana", 28, "bold"), bg="yellow", fg="navy")
        title_lbl.place(x=0, y=0, width=1920, height=45)
        # first image
        img_top = Image.open(r"D:\face_recognition system\college_images\yogesh1.jpg")
        img_top = img_top.resize((1000, 1040), Image.BICUBIC)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1000, height=1040)

        # second image
        img_bottom = Image.open(r"D:\face_recognition system\college_images\yogesh2.jpg")
        img_bottom = img_bottom.resize((1000, 1040), Image.BICUBIC)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=1000, y=45, width=1000, height=1040)

        # button
        Button_btn1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, font=("arial", 18, "bold"),
                              bg="darkgreen", fg="white")
        Button_btn1.place(x=360, y=830, width=300, height=50)

        # =====================Attendance===================

    def mark_attendance(self, i, r, n):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split((","))
                name_list.append(entry[0])

            if (i not in name_list) and (r not in name_list) and (n not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")

    # *************face recognition***********

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []
            conn = mysql.connector.connect(host="localhost", username="root", password="Test@1230",
                                           database="face_recognizer")
            my_cursor = conn.cursor()

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                my_cursor.execute("Select Name from student where Student_id =" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("Select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("Select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Roll No.:{r}", (x, y - 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                    self.mark_attendance(i, r, n)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown Face", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),
                                2)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
