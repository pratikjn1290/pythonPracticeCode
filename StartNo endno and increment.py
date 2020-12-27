value1 = int(input("Enter start value: "))
value2 = int(input("Enter end value: "))
incrementno = int(input("Please enter increament No: "))
if(value1>value2) :
    value1,value2 = value2,value1
for no in range(value1, value2+1, incrementno):
    print(no)
