import mysql.connector
import mysql_details

try :
    mydb = mysql.connector.connect (
        host ='localhost' ,
        user = mysql_details.my_user ,
        password = mysql_details.my_pass 
    )
    print('Connected to MySQL DataBase...')
except :
    print('Error Connection !')
