# methods in string
# 1.index
# 2.slicing
# 3.reversing
# 4.replace
# 5.count
# 6.split
# 8.join
# 9.find
# 10.upper and lowercase
# slicing:
a=('learning python is easy')
print(a[1:8:2])
print(a[:7])
print(a[7:])
print(a[::1])
print(a[::-1])
print(a[::-2])
# index:
b=("ena jock katurengala")
print(b[11])
# reversing
c='bigboss'
print(c[::-1])
# replace
d=('hi,goodmorning')
e=d.replace('goodmorning','good evening')
print(e)
# count
f=('a','a','b','a')
print(f.count('a'))
# split
g=('hi')
r=g.split()
print(r)
# 8.join
h=('jam','ram')
i=''.join(h)
print(i)
# 9.find
j=('pattuchan,meenu')
k=j.find('meenu')
print(k)
# 10.upper and lowercase
l=('udhaya')
print(l.upper())
print(l.lower())
# for loop
fruits=['apple','banana','goa']
for i in fruits:
    print(i)
# while loop
m=('hello')
n=len(m)-1
o=''
while n>=0:
    o=o+m[n]
    n=n-1
    print(o)
# 2
s='learning python is easy'
w=s.split()
l1=[]
i=0
while i< len(w):
    l1.append(w[i][::-1])
    i=i+1
    output=' '.join(l1)
    print(output)
# 3
z=('jeevitha')
y=len(z)-1
x=''
while y>=0:
    x=x+z[y]
    y=y-1
    print(x)