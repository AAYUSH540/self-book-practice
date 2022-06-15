#String slice [q:q] q can positive or negative
st1="0123456789"
print(len(st1))
print("char 0 to 6 - ",st1[0:7])
print("char 7 to end - ",st1[7:])
print("char start to 7 - ",st1[:8])
print("char -5 to -1 - ",st1[-5:-1])
print("char start to ending - ",st1[:])

#[q1:q2:q3] q1-->start q2-->end q3-->gap
print("char start to end with gap of 2 - ",st1[::2])

print(st1[::3]) #[::q] where q is gap between numbers displayeds

#[::q] example
s="ten"
rev_s=s[len(s)::-1]
print(rev_s)
