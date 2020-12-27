no = [ 0 for i in range(10) ]
arr = [ 0 for i in range(10) ]
arr2 = [ 0 for i in range(10) ]

for i in range(0,10):
    no[i] = int(input("No : "))
for i in range(0, 10):
    arr[i] = int(input("No2 : "))
for i in range (0,10):
    arr2[i] = arr[i] + no[i]
    print(arr2[i])
