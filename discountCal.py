amount = int(input("Please enter amount : "))
if amount >= 15000:
    discount = amount*0.15
elif amount >= 10000:
    discount = amount*0.10
elif amount >= 5000:
    discount = amount*0.05
else :
    discount = 0
print("Discount", discount)
