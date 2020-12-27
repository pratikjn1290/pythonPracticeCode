import mysql.connector

con = mysql.connector.connect(user="root", database="test")

curs = con.cursor()

n = input("Enter No Value: ")
name = input("Enter Name: ")
marks = input("Enter Marks: ")

curs.execute("Insert into student(no, name, marks) values (" + n + ",'" + name + "'," + marks + ")")

con.commit()
curs.close()
con.close()
