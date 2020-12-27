value = int(input("Please enter value :"))
sqroot = value ** 2
print(sqroot)
mod = sqroot%10
print(mod)

if mod == value%10 :
    print("Value Is Automorphic")
else :
    print("Value Is Not Automorphic")

