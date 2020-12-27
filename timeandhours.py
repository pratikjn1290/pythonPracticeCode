class timeandhour:
    def __init__(self,h,m):
        self.__hr = h
        self.__min = m
    def __str__(self):
        return "Hour {0} & Minutes {1}".format(self.__hr,self.__min)
    def __add__(self,z):
        totalhr = self.__hr + z.__hr
        totalmin = self.__min + z.__min
        totalhr = totalhr + totalmin // 60 
        totalmin = totalmin % 60
        obj = timeandhour(totalhr, totalmin)
        return obj

x= timeandhour(12,50)
y = timeandhour(5,45)

total = x+y
print(total)
