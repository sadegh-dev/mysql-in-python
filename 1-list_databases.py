import mysql.connector
import mysql_details

mydb = mysql.connector.connect (
    host ='localhost' ,
    user = mysql_details.my_user ,
    password = mysql_details.my_pass 
)

mycursor = mydb.cursor()

stt = "SHOW DATABASES"

mycursor.execute(stt)

for x in mycursor :
    print(x)
