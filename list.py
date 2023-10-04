#important methods in string
# 1.append
# 2.extend (sequence only)
# 3.remove
# 4.pop
# 5.sort(assending order)
# 6.reverse (decending order)
# 7.insert
# 2 methods to access list
# 8.slicing
# 9.index
#--------------------------------------
# 1.append ( append adds a single element to the end and 'int' only accept)
a=[]
a.append(12)
a.append(24)
print(a)
# 2.extend (sequence only) (extend adds multiple elements from a iterable to end of the list)
b=['apple']
b2=['orange']
b.extend(b2)
print(b)
# 3.remove (removes an element based on its value and does not return the removed element)
c=[1,2,3,4]
c.remove(2)
print(c)
# 4.pop (removes an element based on its index and returns the removed element)
d=[10,20,30,40]
print(d.pop(2))
print(d)
# 5.reverse (decending order)
d.reverse()
print(d)
# 6.sort(assending order)
d.sort()
print(d)
# 7.insert(value were inserted based on it index)
d.insert(4,50)
print(d)

# 2 methods to access list
# 8.slicing
e=[1,2,3,4,5,6,7,8]
print(e[2:8:1])
# 9.index
print(e.index(3))
#  for loop in list
list=[]
for i in range(101):
    if i%25==0:
        list.append(i)
        print(list)
#         (or)
for i in range (0,101,25):
    print(i)
# --------------------------------------------------------
a=[3,2,5,1]
a.sort()
print(a)
b=(3,2,5,1)
b.sort()
print(b)
c={3,2,5,1}
c.sort()
print(c)
e=[3,2,5,1]
f=sorted(e)
print(f)
g=(3,2,5,1)
h=sorted(g)
print(h)
i={3,2,5,1}
j=sorted(i)
print(j)