import mysql.connector
import mysql_details


mydb = mysql.connector.connect (
    host ='localhost' ,
    user = mysql_details.my_user ,
    password = mysql_details.my_pass  ,
    database = 'dbnow'
)

mycursor = mydb.cursor()

stt = """

CREATE TABLE person (
    id INT AUTO_INCREMENT KEY ,
    name VARCHAR(255) ,
    address VARCHAR(255)
)

"""

mycursor.execute(stt)
