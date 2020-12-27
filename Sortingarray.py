no = [0 for i in range (5)]
temp = 0
for i in range (0,5):
    no[i] = int(input("Enter Value: "))
for i in range (0,len(no)):
    for j in range (i+1,5):
        if (no[i] > no[j]):
            temp = no[i]
            no[i] = no[j]
            no[j] = temp
for i in range (0,5):
    print(no[i])
        
    
    
