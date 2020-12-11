import mysql.connector

class mydatabase():
    # connect-ing to the sql server
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='Peddirajulu@0'
                                   , auth_plugin='mysql_native_password', database='password_storage')
    # cretating a cursor which acta like a pointer in the database
    mycursor = mydb.cursor()
    # creatig a data base if it doea not exist
    create_data_base = 'CREATE DATABASE IF NOT EXISTS password_storage'
    # seeing all the databases in our local server

    '''creating a table'''
    create_table = 'CREATE TABLE IF NOT EXISTS passwords (id INT AUTO_INCREMENT PRIMARY KEY,application_name VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,password VARCHAR(255) UNIQUE,otp VARCHAR(255),created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'









