startunit = float(input("Please enter start unit :"))
endunit = float(input("Please enter end unit :" ))
totalunit = endunit - startunit
if totalunit <= 100 :
        billprice = totalunit * 5
elif totalunit <= 200 :
    billprice = (100 * 5) + (totalunit-100)*5.50
elif totalunit <= 250 :
    billprice = (100 * 5) + (100 * 5.50) + (totalunit-200)*6.00
else :
    billprice = (100 * 5) + (100 * 5.50) + 300 + (totalunit - 250) * 7
print("Due Bill Payment = " , billprice) 
    
              
              
              
