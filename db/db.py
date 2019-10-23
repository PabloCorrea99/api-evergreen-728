import mysql.connector as mysql 

cnx = mysql.MySQLConnection(
    host="db-server-evergreen-predio.mysql.database.azure.com",
    port=3306,
    user="pcorream@db-server-evergreen-predio", 
    password="Pitufo2013",
    database="evergreen",
)