#write a python program to print the smallest vowel repeating odd number of times 
def smvov(word):
    count=0
    for i in word:
        s=0
        if i in "aeiouAEIOU":
            if word.count(i)%2!=0:
                word.count(i)=n
                print(min(s))
word=input()
s=0
print(smvov(word))

