#while
i=23
while i>11:
    print(i)
    i=i-2

#employee pay rate
emp_no=3
while emp_no>0:
    hours,rate=eval(input("hours and rate : "))
    pay = hours*rate
    print(f"Employee {emp_no} Pay ----> {pay}")
    emp_no-=1

print("\n")
#factorial
fac=int(input("Factorial num = "))
ans=1
while fac > 1:
        ans=ans*fac
        fac-=1
print("Factorial = ",ans)

print("\n")
#print 1 to 10 on same line
count=10
while count>0:
    print(count,end=",")
    count-=1
print("\nEND")

print("\n")
#average of all entered numbers
num=0
total=0
count=0
while num>=0:
    num=int(input("NUMBER (Negative to exit) = "))
    total+=num
    count+=1
    avg=total/count
print("AVERAGE = ",avg)

#infinite while
i=1
while True:
    if i%3==0:
        break
    else:
        print(i)