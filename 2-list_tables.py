import mysql.connector


mydb = mysql.connector.connect (
    host ='localhost' ,
    user = 'debian-sys-maint' ,
    password = 'xkfnnlgUOSuVdAjg' ,
    database = 'dbnow'
)

mycursor = mydb.cursor()

stt = "SHOW TABLES"

mycursor.execute(stt)

for tb in mycursor :
    print(tb)
