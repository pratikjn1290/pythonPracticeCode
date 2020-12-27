class bank:
    def getinfo(self):
        self.__no = int(input("Account No :"))
        self.__name = input("Name : ")
        self.__bal = int(input("Opening Balance : "))
    def show(self):
        print("---> {0} : {1} : {2}".format(self.__no, self.__name, self.__bal))
#        print("---> ", self.__no, " : ", self.__name, " : ", self.__bal)
    def deposit(self, amt):
        self.__bal += amt
    def withdraw(self, amt):
        if amt + 5000 <= self.__bal:
            self.__bal -= amt
            return True
        else:
            return False

bk = []
choice = 0
count = 0
num = 0
amount = 0
while choice != 6:
    print("-------------------")
    print("1. Add Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display")
    print("5. List")
    print("6. Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        bk.append(bank())
        bk[count].getinfo()
        count += 1
    elif choice == 2:
        num = int(input("Number : "))
        amount = int(input("Amount to Deposit : "))
        bk[num-1].deposit(amount)
    elif choice == 3:
        num = int(input("Number : "))
        amount = int(input("Amount to Withdraw : "))
        if bk[num-1].withdraw(amount):
            print("Amount withdrawan")
        else:
            print("Balance not enough")
    elif choice == 4:
        num = int(input("Number : "))
        bk[num-1].show()
    elif choice == 5:
        for x in bk:
            x.show()
print("Bye")
