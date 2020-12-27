class item:
    def show(self):
        self._code = input("Enter Item Code : ")
        self.name = input("Enter Item Name : ")
        self._rate = int(input("Enter Item Rate : "))
class sale (item):
        def quantity(self):
            self._qty = int(input("Enter Item Quantity :"))
class scheme:
    def schemeperc(self):
        self._dis = int(input("Enter Item Discount :"))
class bill (sale, scheme):
    def billcalc(self):
        price = self._qty * self._rate
        discount = (price * self._dis) / 100
        finalbill = price - discount
        print(finalbill)

x = bill()
x.show()
x.quantity()
x.schemeperc()
x.billcalc()
        
        
