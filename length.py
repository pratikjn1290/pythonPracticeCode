number = int(input("Enter Number: "))
temp = 0
while (number>0) :
    temp = temp * 10
    mod = number % 10
    temp = temp + mod
    number = number // 10
print(temp)
