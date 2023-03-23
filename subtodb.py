#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
print("Content-Type:text/html")
print()
import cgi
import base64
from Crypto.Cipher import AES

from Crypto.Util.Padding import pad,unpad


print("<h1 style=\"color:green;\">Feedback Data Submitted successfully</h1>")
print("<p>Stored in the database</p>")
print("<hr/>")
print("<body bgcolor='white'>")



form = cgi.FieldStorage()
student_id = form.getvalue("student-id")
question_1 = form.getvalue("question-1")
question_2 = form.getlist("question-2")

import mysql.connector
# connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="feedbacks"
)

cursor = db.cursor()

# student_id = str(student_id).encode()
# question_1 = str(question_1).encode()
# question_2 = str(question_2).encode()


iv =  'BBBBBBBBBBBBBBBB'.encode('utf-8') #16 char for AES128

key ='A71je7R8iR997i7e'

#######################################################
# Encryption function

def encrypt(data,key,iv):
        data= pad(data.encode(),16)
        cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
        output= base64.b64encode(cipher.encrypt(data))
        return output

# Decryption function
def decrypt(enc,key,iv):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        output = unpad(cipher.decrypt(enc),16)
        return output



fblist = [student_id, question_1, question_2]


ciper_list = []

for value in fblist:
    ciper_list.append(encrypt(str(value), key, iv))



plain_text = []

# print(ciper_list)

# store data in a MySQL database
# cursor.execute("INSERT INTO feedbacks (student_id, question_1, question_2) VALUES (%s, %s, %s)", (student_id, question_1, question_2))
cursor.execute("INSERT INTO feedbacks (student_id, question_1, question_2) VALUES (%s, %s,%s)", (ciper_list[0], ciper_list[1],ciper_list[2]))
db.commit()


cursor.execute("SELECT student_id FROM feedbacks")
rows = cursor.fetchall()

# Decrypt the data
print("<br>")

# close the database connection
cursor.close()
db.close()

print("Feedback submitted successfully!")

print("<br>")

print("<a href='http://localhost/protnew/decrypt.py'>Click hear to view submitted students</a>")

print("<br>")
print("<a href='http://localhost/protnew/'>Click hear to go to the main page </a>")

print("<br>")
print("<a href='http://localhost/protnew/decrypt_answers.py'>Click hear to go to view the answers </a>")