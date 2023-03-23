#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
print("Content-Type:text/html")
print()
import mysql.connector
from mysql.connector import Error
import cgi
import base64
from Crypto.Cipher import AES

from Crypto.Util.Padding import pad, unpad
print("<head> <link rel=\"stylesheet\" href=\"style.css\"></head> ")
print("<center>")
print("<h1 style=\"color:green;\">Feedback form - Submitted answers</h1>")
print("<p>Feedback answers will display here.</p>")
print("</center>")
print("<hr>")
print("<body bgcolor='white'>")



def decrypt(enc, key, iv):
    enc = base64.b64decode(enc)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc), 16)



iv =  'BBBBBBBBBBBBBBBB'.encode('utf-8') #16 char for AES128

key ='A71je7R8iR997i7e'



import mysql.connector
# connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="feedbacks"
)

cursor = db.cursor()


cursor.execute("SELECT question_1,question_2 FROM feedbacks")
rows = cursor.fetchall()

# Decrypt the data
print("<table>")

# Create the table headers
print("<tr>")
print("<th>Submitted answers for question 1</th>")
print("<th>Submitted answers for question 2</th>")
print("</tr>")

# Decrypt the data and add each row to the table
for row in rows:
    ciphertext1 = row[0]
    ciphertext2 = row[1]
    plaintext1 = decrypt(ciphertext1, key, iv)
    plaintext2 = decrypt(ciphertext2, key, iv)
    print("<tr>")
    print("<td>{}</td>".format(plaintext1.decode("utf-8", "ignore")))
    print("<td>{}</td>".format(plaintext2.decode("utf-8", "ignore")))
    print("</tr>")


# Close the table
print("</table>")


# close the database connection
cursor.close()
db.close()

print("<hr/>")
print("<a href='http://localhost/protnew/'>Click hear to go to the main page </a>")

print("<br>")
print("<a href='http://localhost/protnew/decrypt.py'>Click hear to view submitted students</a>")
