#empty tuple
a=(1,)
print(type(a))

T=(10,20,10,10,20,30,40,50,60)
#count
print(T.count(10))
#index
print(T.index(20))
#min
print(min(T))
#max
print(max(T))
#sorted (it converts tuple into list in orderwise)
print(sorted(T))
#length
print(len(T))
# list comprehension:
s=[ n*n for n in range(1,11)]
print(s)
a=[i for i in range(1,11) if i%2!=0]
print(a)
b=[i for i in range(1,11) if i%2==0]
print(b)