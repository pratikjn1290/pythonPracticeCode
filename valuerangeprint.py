value1 = int(input("Enter first value:"))
value2 = int(input("Enter second value:"))            
if value1>value2 :
    value2,value1 = value1,value2
    print(value1)
    print(value2)
for no in range(value1, value2+1):
    print(no)
