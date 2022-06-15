#string formate
#defualt place
st1=str(input("String 1 : "))
st2=str(input("String 2 : "))
st3=str(input("String 3 : "))
print("{} ----> {}".format(st1,st2))

#String formate types
#positional
print("{2} ---> {1} ----> {0}".format(st1,st2,st3))

#keyword
print("{e} ---> {g} ----> {b}".format(e=st1,g=st2,b=st3))

#integer-->binary representation and float-->exponent representation
print("{0:b} ----> {0:e}".format(213,23.234))

#rounding off integers
print("{0:.2f}".format(2/25))

#String alignment
print("{:^9} | {:>9} | {:<9}".format(st1,st2,st3))

#membership op in & not in ---->true or false
print("a" in st1)
print("s" not in st1)

#unicode (16-bit) and ascii (8-bit) ecoding
#ord takes char returns ascii or unicode value
print(ord("a")) #char to the integer

#chr takes ascii or unicode value and returns char
print(chr(106)) #integer to char