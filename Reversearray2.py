no = [0 for i in range (0,10)]
for i in range (0,10):
    no[i] = input("Please enter no: ")    
for i in range(0,5):
    temp = no[i]
    no[i] = no[9-i]
    no[9-i] = temp
for i in range(0,10):
    print(no[i])
