number1 = int(input("Please Enter first number : "))
number2 = int(input("Please Enter second number : "))
number3 = int(input("Please Enter third number : "))
if number1 > number2 and number1 > number3 :
    print("Large number", number1)
elif number2 > number3 and number2 > number1: 
    print("Large number", number2)
else :
    print("Large number", number3)
