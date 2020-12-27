no = [0 for i in range (5)]
for i in range (0,5):
    no[i] = int(input("Enter Value: "))
min = no[0]
max = no[0]
for i in range (0,5):
    if no[i]>max:
        max = no[i]
    if no [i] < max:
        min = no[i]     
print("Minimum Value:", min)
print("Maximum Value:",max)
