#break and continue
val=0
while True:
    val+=1
    if val%13==0:
        break #breaks out of loop
    if val%3==0:
        continue #skipps remaining body of loop and goes to next loop
    if val%5==0:
        pass #passes the condition without anything
    print(val)

num=int(input("ASSSERTING VALUE : "))
assert num>0 #true - > then executes otherwiser gives assertionerror with ####
print("ENTERED NUM = ",num)



