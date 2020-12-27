no = [0 for i in range (5)]
for i in range (0,5):
    no[i] = int(input("Please enter no: "))
x = int(input("Please enter to search record: "))
flag = False
for i in range(0,5):
    if no[i] == x:
        pos = i+1
        flag = True
        print("Position of search record", pos)

if flag == False:
    print("Not Found")

