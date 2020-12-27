number = int(input("Enter Number: "))
flag = 0
for value in range (2, number):
    if number % value == 0 :
        flag = 1
        break

if flag == 0 :
    print("Number is prime")
else :
    print("Not Prime")
    
