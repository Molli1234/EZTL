#to print count of vowels in even and odd positions#
s1=input()
s="a,e,i,o,u,A,E,I,O,U"
ecount,ocout=0
for i in range(len(s)):
    if i%2==0:
        if s1[i] in "a,e,i,o,u,A,E,I,O,U":
            ecount+=1
    else:
        if s1[i] in "a,e,i,o,u,A,E,I,O,U":
            ocount+=1
print(ecount,ocount)
 
