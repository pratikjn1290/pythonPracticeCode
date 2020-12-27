number = int(input("Enter Number: "))
sum = 0
while (number>0) :
    mod = number%10
    sum = sum + mod
    number = number // 10
print(sum)
