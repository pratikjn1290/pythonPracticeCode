class employeedetails:
    def employeeinfo(self):
        self.__empid = int("Employee Id :"))
        self.__name = int("Employee Name :"))
        self.__class = int("Employee class :"))
    def show(self) :
        print("---> {0} : {1} : {2}".format(self.__empid, self.__name, self.__class))

    def addemployee(self,EID, ENAME,EPMCLS):
        x = employeedetails()
        x.employeeinfo()
