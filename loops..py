#for loop (string)
fruits=['apple','mango','goa']
for i in fruits:
    print(i)
    # or
for i in range(10):
    print(fruits)
# -----------------------------------------------------------------------------------
# dictionary (occurance)
word=input('enter the word')
d={}
for x in word:
    d[x]=d.get(x,0)+1
    for k,v in d.items():
        print(k,v)
# -----------------------------------------------------------------------------------
# write a program to find no.of occurance of each vowels present in the given string.
word='jeevitha manikandan'
d={}
vowels=('aeiou')
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,v)
# -----------------------------------------------------------------------------------
# excercise:
a='A4C2B1Z8'
s1=s2=output=" "
for i in a:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i
for i in sorted (s1):
        output=output+i
for i in sorted (s2):
        output=output+i
print(output)
# -----------------------------------------------------------------------------------
a='A4@C2$B1Z^8'
s1=s2=s3=output=" "
for i in a:
    if i.isalpha():
        s1=s1+i
    elif i.isnumeric():
        s2=s2+i
    else:
        s3=s3+i
for i in sorted (s1):
        output=output+i
for i in sorted (s2):
        output=output+i
for i in sorted(s3):
        output=output+i
print(output)
# -------------------------------------------
# While loop:
s=('jeevitha')
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
print(target)
# -----------------------------------------------------------------------------------
a='hi how are you'
b=a.split()
c=[]
i=0
while i<len(b):
    c.append(b[i][::-1])
    i=i+1
    d=' '.join(c)
    print(d)
# -----------------------------------------------------------------------------------
# odd and even letters print
e='learning python is easy'
i=0
while i<len(e):
    print(e[i])
    i+=2
#     or
i=1
while i<len(e):
    print(e[i])
    i+=2
# -----------------------------------------------------------------------------------
# to print collab of names
a='acegi'
b='bdfhi'
c=''
i,j=0,0
while i<len(a):
    if i<len(a):
        c=c+a[i]
        i+=1
    if i<len(b):
        c=c+b[j]
        j+=1
print(c)
