#take value and print absolute
absolute=int(input("Val = "))
print("|",absolute,"|","=",absolute if absolute>0 else -absolute,)

#read 2 no.s and print quotant
divisor,divider=eval(input("Enter 2 No.s = "))
if divider!=0:
    print(divisor,"/",divider,"=",divisor/divider)
else:
    print("Divider is 0")

#tax calculator
sal=float(input("Tax! = "))
if sal<5000:
    taxamt=0.05*sal
elif sal<6000:
    taxamt=0.06*sal
elif sal<7000:
    taxamt=0.07*sal
else:
    taxamt=0.1*sal
print("Salary = ",sal,"Taxamount = ",taxamt)