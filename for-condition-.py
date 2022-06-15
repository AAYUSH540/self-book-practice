#for basics
for i in [1,3,4,53,4,54]:
    print(i*2)

print("\n")
for i in range(12):
    print(i)

print("\n")
for i in range(2,23,9):
    print(i)

print("\n")
#print even and odd numbers
print("ODD : ")
for i in range(1,100,2):
    print(i)

print("\n")
#multiplication table
multiplication_number=int(input("ENTER MUL NUM : "))
for i in range(11):
    print(f"{multiplication_number} * {i} = {multiplication_number*i}")

#print adcii code for given string
string=input("ENTER STRING : ")
for c in string:
    print(ord(c),end="")

print("\n")
#print all prime numbers in given range
prime=int(input("PRIME LIMIT : "))
for a in range(1,prime+1):
    k=0
    for i in (2,a//2+1):
        if a%i==0:
            k+=1
    if k<=0:
        print(a)
        


