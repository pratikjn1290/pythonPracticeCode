class rect:
    def __init__(self, l,h):
        self.__lenght = l
        self.__height = h
    def __str__(self):
        return "Area {0}".format(self.__lenght * self.__height)
    def __gt__(self, other):
        ar1 = self.__lenght * self.__height
        ar2 = other.__lenght * other.__height

        if ar1 > ar2:
            return True
        else:
            return False

    def __eq__(self, other):
        ar1 = self.__lenght * self.__height
        ar2 = other.__lenght * other.__height
        if ar1 == ar2:
            return True
        else:
            return False

r1 = rect(3,4)
r2 = rect(3,5)

if r1 > r2 :
    print (r1)
else :
    print(r2)
if  r1 == r2 :
    print("Both are same")
else :
    print("Both are not same")
