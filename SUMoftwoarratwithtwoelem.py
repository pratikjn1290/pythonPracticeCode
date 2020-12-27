no = [ 0 for i in range(10) ]
sum = [0 for i in range (5)]
for i in range(0,10):
    no[i] = int(input("No : "))
for i in range (0,5):
    sum[i] = no[i*2] + no[(2*i)+1]
    print(sum[i])
