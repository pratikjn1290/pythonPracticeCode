basic = int(input("Please enter basic amount : "))
if basic >= 10000:
    HRA = basic*0.25
    DA = basic*0.15
    IT = basic*0.20
elif basic >= 5000:
    HRA = basic*0.15
    DA = basic*0.05
    IT = basic*0.10
else :
    DA = 0
    IT = 0
    HRA = basic*0.05
Salary = basic + HRA + DA -IT
print("Monthly Net Salary of Employee", Salary)
