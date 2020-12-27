number = int(input("Enter Number: "))
temp = number
sum = 0
while (number>0) :
    mod = number%10
    qube = mod ** 3
    sum = sum + qube
    number = number // 10
print(sum)
if sum == temp :
    print("Armstrong Number")
else :
    print("Normal")
