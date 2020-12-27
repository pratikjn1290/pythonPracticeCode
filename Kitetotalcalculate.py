kites = int(input("Enter Number of Kites : "))
if kites >= 50 and kites < 100 :
    total = kites * 6
elif kites >= 100 and kites < 150 :
    total = kites * 5.50
elif kites >= 150 and kites < 200 :
    total = kites * 5.00
else :
    total = kites * 4.00
print ("Total Price of Kites", total)    



