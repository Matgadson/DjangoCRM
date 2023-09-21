import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'Matome',
    user = 'Admin1',
    passwd = 'con.pass.A.12!',
    auth_plugin = 'mysql_native_password'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")
print("Database created successfully")