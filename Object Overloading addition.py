class amountandpaisa:
    def __init__(self,r,p):
        self.__r = r
        self.__p = p
    def __str__(self):
        return "Rupees {0} & Paise {1}.format(self.__rs,self.__p)"
    def __add__(self,z):
        totalrs = self.__rs + z.__rs
        totalp = self.__p + a1.__p
        totalrs = totalrs + totalp // 100
        obj = amountandpaisa(totalrs, totalp)
        return obj

x= amountandpaisa(12,50)
y = amountandpaisa(5,70)

total = x+y
print(total)
