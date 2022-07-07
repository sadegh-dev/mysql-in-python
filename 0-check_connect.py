import mysql.connector


try :
    mydb = mysql.connector.connect (
        host ='localhost' ,
        user = 'debian-sys-maint' ,
        password = 'xkfnnlgUOSuVdAjg'
    )
    print('Connected to MySQL DataBase...')
except :
    print('Error Connection !')
