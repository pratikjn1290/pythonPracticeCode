itemname = input("Please enter itemname : ")
rate = float(input("Price of the item : "))
quantity = int(input("Quantity of the item : "))
amount = quantity * rate
dis = 0
if itemname == "a" or itemname == "A" :
    if quantity > 50 :
        dis = amount * 0.20
    else :
        dis = amount * 0.10
elif itemname == "b" or itemname == "B" :
    if quantity > 10 :
        dis = amount * 0.15
    else :
        dis = amount * 0.05
        
netpay = amount - dis
print(netpay)    
