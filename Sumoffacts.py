# 1 - 1/2! + 1/3! - 1/4! + 1/5! - 1/6! …… - 1/10!
sum = 0
for i in range(1, 11):
    fact = 1
    for n in range (1,i+1) :
        fact = fact*n
    if i % 2 ==0 :
        sum = sum - 1/fact
    else:
        sum = sum + 1/fact
print(sum)            

