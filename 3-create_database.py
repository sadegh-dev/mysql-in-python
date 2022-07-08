import mysql.connector


mydb = mysql.connector.connect (
    host ='localhost' ,
    user = 'debian-sys-maint' ,
    password = 'xkfnnlgUOSuVdAjg' ,
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
