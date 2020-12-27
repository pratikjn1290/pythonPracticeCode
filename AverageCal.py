class average:
    def xyz(self):
        self.__no1 = int(input("No 1 :"))
        self.__no2 = int(input("No 2 :"))
        self.__no3 = int(input("No 3 :"))
    def avg(self):
        self.__avg = ((self.__no1+self.__no2+self.__no3)/3)
        print(self.__avg)
print("Average Calculation")
obj = average()
obj.xyz()
obj.avg()
    
