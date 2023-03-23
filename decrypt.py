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
print("<h1 style=\"color:green;\">Feedback form - Submitted students</h1>")
print("<p>Students who have submitted the form will display here.</p>")
print("<hr/>")
print("<body bgcolor='white'>")
print("</center>")


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


cursor.execute("SELECT student_id FROM feedbacks")
rows = cursor.fetchall()

# Decrypt the data
print("<br>")

print("<table>")

# Create the table headers
print("<tr>")
print("<th>Submitted Student ID's</th>")
print("</tr>")

# Decrypt the data and add each row to the table
for row in rows:
    ciphertext = row[0]
    plaintext = decrypt(ciphertext, key, iv)
    print("<tr>")
    print("<td>" + plaintext.decode("utf-8", "ignore") + "</td>")
    print("</tr>")

# Close the table
print("</table>")





# close the database connection
cursor.close()
db.close()
print("<a href='http://localhost/protnew/'>Click hear to go to the main page </a>")