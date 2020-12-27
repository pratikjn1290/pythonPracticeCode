rupees = int(input("Enter RS: "))
note = [ 0 for i in range(10) ]
currency = [2000,500,200,100,50,20,10,5,2,1]
for i in range(0,10):
    note[i] = rupees // currency[i]
    rupees = rupees % currency[i]
    print(note[i], currency[i])
