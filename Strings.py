# '' "" """"""
st1='aayush'
st2="Aayush"
st3="""Fadia
Aayush""" #multiline string
print(f"{st1} , {st2} , {st3}")

#backslash use \
#1 this continue the string even if line changes for easy reading
st4='Fadia \
Aayush D'
print(st4)

#2 \ used to escape quote chars inside '' or ""
st5="Fadia : \"My name is you know already\""
st6='Aayush : \'Yes ,birather from another miather\''
st7="Me : next \n line"
print(st5,st6,st7)

print(type(st5)) #used to identify type of "" inside type()

# + concatation
print(st5+st6)

# * repetition
print(st2*3)

#character access
st8="ABCD"
print(st8[1])
print(st8[-2])

#length
print(len(st8))

#Strings immutable once declred cant change itself \
st9="Strings"
st10="My " + st9
print(st10)

del st10 #deletes st10
