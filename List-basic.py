# 1 contains any datatype also mutable
l1=[1,2,3]
l2=["aas","sdx","dfaw"]
l3=[1.2,"asda",[2,3]] #nested list
l4=[] # empty list

print()

# 2 input
l5=list(input("List = ")) # input taken as string
print(l5)

l6=eval(input("List(eval) = "))
print(l6)

print()

# 3 list() ----> string to list of characters
s3="JLKSA"
print("list(JLKSA) = ",list(s3))

s4=list() # 4 create empty list

print()

# 5 split() ----> sentence into words
s5="work is worship"
print(f"{s5}.split() = ",s5.split())

print()

# 6 multidimentional list 3*3
matrix=[[1,2,3],[12,23,44],[34,45,28]]
print("matrix = ",matrix)

print()

# 7 create a list of n integers
int_list=[]
n=int(input("Length of list ::: "))
for i in range(n):
    k=int(input("Value : "))
    int_list.append(k)
print("Int_List = ",int_list)

print()

# 8 indexing
l8=[1,2,3,4,['!','!','$','&']]
print("Indexing :")
print(f"l8 = {l8}")
print(f"l8[1] = {l8[1]} , l8[-1] = {l8[-1]} , l8[2] = {l8[2]} , l8[4][2] = {l8[4][2]}")

print()

# 9 slicing
l9=[1,2,3,4,5,6,7,8]
print("Slicing :")
print(f"l9 = {l9}")
print(f"l9[0:3] = {l9[0:3]} , l9[-4:-1] = {l9[-4:-1]} , l9[6:] = {l9[6:]} , l9[6:0:-2] = {l9[6:0:-2]} , l9[::3] = {l9[::3]}")

print()

# 10 traversing
# for and while
print("Traversal ::: ")
print("For :")
l10=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
for i in l10:
    if i//2 == 0:
        print(i)

print()

print("While : ")
i=0
while i<10:
    print(l10[i])
    i+=1

print()

# 11 printing positive negative index
l11=[1,2,3,4,5,6,7,8]
for i in range(len(l11)):
    print(f"{l11[i]} ----> Positive index = {i} , Negaive index = {i-len(l11)}")
