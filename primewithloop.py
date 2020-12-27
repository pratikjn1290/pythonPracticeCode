for i in range (1, 101) :
    flag = True
    for n in range (1,  i+1) :
        if i % n == 0 :
            flag = False
    if flag == True:
        print(i)
