no = [ 0 for i in range(10) ]
arr = [ 0 for i in range(10) ]

for i in range(0,10):
    no[i] = int(input("No : "))
for i in range(0, 10):
    arr[i] = no[9-i]
    print(arr[i])
