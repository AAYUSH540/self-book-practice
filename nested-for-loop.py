num=int(input("NUM = "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("\n")

for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

for i in range(1,num+1):
    for j in range(num,i,-1):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    for l in range(1,i):
        print("*",end=" ")
    print()

print()

for i in range(num+1):
    for j in range(i):
        print(j+1,end="")
    print()
