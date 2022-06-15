# 1 creation
d1_1={} #empty dictionary
d1_2={1:"aqw",2:"sdsd","a":"asds","rfr":[1,23,4,5]}
print(d1_1,d1_2)

# key can be number,string,tuple
# value can be anything
# order can be anything in dictionary
# case-sensitive
# dict is modifieable
# dict is unordered collection of objects

print()

print("Type = ",type(d1_1))

print()

# 2 initialization and accessing elements
d2_1=dict({1:"fhrs",2:"ghh"}) # rarely used built-in function dict()

d2={
    'name':'aayush',
    'age':'18',
    'blood-group':'o+'
}

print("d2 = ",d2)

print(f"Name  = {d2['name']} , Age = {d2['age']} , Blood-group = {d2['blood-group']})")
# accessing element with d2['q'] q is key

print()

# print(d2['middle-name']) # gives keyerror

# get() is used to avoid keyerror
print(f"d2.get('middle-name') = {d2.get('middle-name')}")# give none if key is not in dictionary

print()

print(f"'salary' in d2 = {'salary' in d2}") # in is used to check key in dict

print()

# 3 traversing in dictionary

d3={
    1:'a',
    2:'b',
    3:'c',
    4:'d'
}
print(f"d3 = {d3}")
for i in d3:
    print(f"{i} = {d3[i]}")

print()

# 4 appeding and updating

d4={
    'a':'apple',
    'b':'ball',
    'c':'cat',
    'd':'dolby'
}
print(f"d4 = {d4}")

d4['e']='elaboration'
print(f"d4['e']='elaboration' ----> d4 = {d4}") # appending value

d4.update({'e':'establishment'})
print("d4.update({'e':'establishment'}) ----> d4 = ",d4) # updating value

print()

# 5 removing dictionary elements and dictionary

d5=d4
del d5['e']
print("del d5['e'] ----> d5 = ",d5) # deleting 'e' key value from d5

d5.clear()
print("d5.clear()  ----> d5 = ",d5) # clear all key value from d5 but d5 dict exist

del d5
# print("del d5  ----> d5 = ",d5) # delete d5 from existence

print()

# 6 sorting key and value
d6={
    'z':1,
    'd':2,
    'c':3,
    'b':4
}

print("d6 = ",d6)
print("Key-sorted : ")
for k in sorted(d6):
    print(k,d6[k])

print()

print("Value-sorted : ")
for v in sorted(d6,key=d6.get):
    print(v,d6[v])

print()

# ex enter multiple student name and marks and store in dict and print accordingly
n=int(input("Number of students = "))
record=dict()

for i in range(n):
    name=str(input("Name = "))
    per=float(input("Percentage = "))
    record[name]=per

print(f" name \t\t percentage")
for i in sorted(record,key=record.get):
    print(f" {i} \t\t {record[i]}")

print()

# 7 dictionary functions and methods

d7_1=dict() # 1 dict() method for creating dictionary

d7={
    'reyna':'duelist',
    'chamber':'sentinel',
    'breach':'initiator',
    'skye':'initiator',
    'raze':'duelist',
    'yoru':'duelist',
    'sage':'sentinel'
}

print(f"d7 = {d7}")
print(f"len(d7) = {len(d7)}") # 2 len(q) length of dict ----> q is dict

print()

d7_2=d7.clear
print(f"d7_2.clear = {d7_2}") # 3 q.clear() clears dict

print()

print(f"d7.get('reyna') = {d7.get('reyna')}") # 4 q.get(key) to access value of defined key

print()

print(f"d7.pop('reyna') = {d7.pop('reyna')}") # 5 q.pop(key) prints value of key defined and delete that key:value
print(f"d7 = {d7}")

print()

print(f"d7.popitem() = {d7.popitem()}") # 6 q.popitem() prints value of last key and removes last key:value
print(f"d7 = {d7}")

print()

print(f"d7.keys() = {d7.keys()}") # 7 q.keys() prints all keys

print()

print(f"d7.values() = {d7.values()}") # 8 q.values() prints all values

print()

print(f"d7.items() = {d7.items()}") # 9 q.items() prints all keys:values

print()

# 8 program that takes key:value from user and then converts dict in list of tuples
d8=dict()
n=int(input("Dictionary length : "))
i=0
while i<n:
    i1=input("Enter key:value = ")
    i2=i1.split(':')
    d8[i2[0]]=i2[1]
    i+=1

print(f"d8 = {d8}")

items=list(d8.items())

for i in items:
    print(f"{len(i)} , {i}")

print()

# 9 counting freaquency of characters

sentence="Computer is a Machine"
d9={}
for i in sentence:
    d9[i]=d9.get(i,0) + 1 # 0 is defining value for key
print(f"d9 = {d9}")






