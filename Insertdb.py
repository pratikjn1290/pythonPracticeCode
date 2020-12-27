import mysql.connector

con = mysql.connector.connect(user="root", database="test")

curs = con.cursor()

n = input("Enter No Value: ")
marks = input("Enter Marks: ")

cmd = "update student set marks = (%s) where no = (%s);"
value = (marks, n)

curs.execute(cmd, value)

con.commit()
curs.close()
con.close()
