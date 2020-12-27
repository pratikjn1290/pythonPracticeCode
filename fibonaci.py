no1 = 1
no2 = 2
print(no1)
print(no2)

for no in range (1,19):
    no3 = no1+no2
    print(no3)
    no1,no2 = no2,no3
print("---end---")
