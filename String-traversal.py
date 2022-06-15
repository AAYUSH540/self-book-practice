st1="abcdefghijkl"
for i in st1:
    print(i)

print()

i=0
while i<len(st1)/2:
    print(st1[i])
    i+=1

#find length of entered string
st2=""
while True:
    if st2=="quit":
        break
    else:
        st2=input("String(\"quit\" to exit) ::: ")
        print(len(st2))

print()

#change / replace slice of string using "replace"
st3=str(input("String ::: "))
st4=str(input("Enter slice of String to be change : "))
st5=str(input("Slice to change : "))
st6=st3.replace(st4,st5)
print(st6)

print()

