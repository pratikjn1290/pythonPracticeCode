no = int(input("Enter Decimal Value: "))
arr = [0 for i in range(8)]   

for i in range (8):
    if (no%2==0):
        arr[i] = 0 
    else :
        arr[i] = 1    
print(arr[::-1])  
    

    
