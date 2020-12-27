import mysql.connector

con = mysql.connector.connect(user="root", database="test")

curs = con.cursor()

n = input("Enter number ")

cmd = "delete from student where no = (%s);"

value = (n, )

curs.execute(cmd, value)

con.commit()

curs.close()

con.close()

input()
