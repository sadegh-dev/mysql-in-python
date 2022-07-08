import mysql.connector


mydb = mysql.connector.connect (
    host ='localhost' ,
    user = 'debian-sys-maint' ,
    password = 'xkfnnlgUOSuVdAjg'
)

mycursor = mydb.cursor()

stt = "SHOW DATABASES"

mycursor.execute(stt)

for x in mycursor :
    print(x)
