import mysql.connector
import mysql_details


mydb = mysql.connector.connect (
    host ='localhost' ,
    user = mysql_details.my_user ,
    password = mysql_details.my_pass ,
    database = 'dbnow'
)

mycursor = mydb.cursor()

stt = "SHOW TABLES"

mycursor.execute(stt)

for tb in mycursor :
    print(tb)
