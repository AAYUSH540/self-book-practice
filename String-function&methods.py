# 1 len() finds total length of string
st1=str(input("String = "))
print(f"len({st1}) = {len(st1)}")

print()

# 2 count() counts perticuler character
print(f"count('a') = {st1.count('a')}")

print()

# 3 find() shows index of given character ------->output -1 means substring not found
print(f"find('a') = {st1.find('a')}")   #first occurance
print(f"find('a',3) = {st1.find('a',3)}")   #from start position occurance
print(f"find('a',4,7) = {st1.find('a',4,7)}")   #from start to end(not end postion) position occurance
print(f"find('aa',1) = {st1.find('aa',1)}")

print()

# 4 lower() upper()
print(f"lower({st1}) = {st1.lower()}")
print(f"upper({st1}) = {st1.upper()}")

print()

# 5 islower() isupper() ----> returns boolean for lower or upper
print(f"islower({st1}) = {st1.islower()}")
print(f"isupper({st1}) = {st1.isupper()}")

print()

# 6 capitalize gives copy of string with first letter capital
print(f"capitalize({st1}) = {st1.capitalize()}")

print()

# 7 isalnum() returns true if it contains only numbers and character (alphanumeric characters excluding specials and space)
## false for !,@,#,$,%,^,&,*,(,),' ',',' (anything otherthan char and num)
print(f"isalnum({st1}) = {st1.isalnum()}")

print()

# 8 isalpha() ---->only chars isalnum() ---->only digits
print(f"isalpha({st1}) = {st1.isalpha()}")
print(f"isdigit({st1}) = {st1.isdigit()}")

print()

# 9 lstrip()
print(f"lstrip({st1}) = {st1.lstrip()}") # default --> removes left space
print(f"lstrip({st1},removing a) = {st1.lstrip('a')}") #  removes specified left substring

print()

# 9 rstrip()
print(f"rstrip({st1}) = {st1.rstrip()}") # default --> removes right space
print(f"rstrip({st1},removing a) = {st1.rstrip('a')}") #  removes specified right substring

print()

# 10 isspace() ----> true if contains only space
st10="      "
print(f"isspace('     ') = {st10.isspace()}")

print()

# 11 istitle() ----> returns true if every first character of words in sentence is capital
st11="This Is Example Yes"
print(f"istitle({st11}) = {st11.istitle()}")

print()

# 12 replace(q1,q2) ----> replace q1 with q2
st12="This is a war which is not great"
print(f"replace({st12},'is','was') = {st12.replace('is','was')}")

print()

# 13 split() ----> splits sentence in word
st13="'Split' 'in' 'words'"
st13_1=st13.split()
print(f"spilt({st13}) = ")
for i in st13_1:
    print(i)

print()

print(f"spilt({st13},seporator=') = ")
st13_2=st13.split("'")
for i in st13_2:
    print(i)

print()

# 14 join() concates words from list ----> send copy to an empty string
st14=["String--1 ","String--2 ","String--3 ","String--4 "]
st14_1=""
print(f"join({st14}) = {st14_1.join(st14)}")

print()

# 15 swapcase() change case
st15="SwapiNg CasEs"
print(f"swapcase({st15}) = {st15.swapcase()}")

print()

# 16 partition(q) ---->  split string in three parts at first occurence of the q
st16_1="Partioning at bunker alpha"
print(f"partition({st16_1}) = {st16_1.partition('at')}")

st16_2="Partioning at bunker alpha"
print(f"partition({st16_2}) = {st16_2.partition('atas')}") # if substring not in sentence then gives 2 empty string at end

print()

# 17 str() ----> any data to string
print(f"str(233) = {str(233)}")
