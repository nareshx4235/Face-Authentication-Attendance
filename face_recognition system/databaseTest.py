import mysql.connector

conn=mysql.connector.connect(host="localhost",username="root",password="Test@1230",database="face_recognizer")
cursor=conn.cursor()
cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()