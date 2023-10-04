# duplicates removed and unique value represented.
#no slicing, index, not preserved.
# it's mutable so we can add and remove data.
# no insort.
a=set()
#empty set were decleard by a=set()
print(type(a))
s={1,1,3,4,5,5,2,2}
print(s)
# add
l=(6,7,8,9)
# (or)
l=[6,7,8,9]
s.update(l)
print(s)
s.remove(7)
print(s)
s.discard(2)
print(s)
s.clear()
print(s)
# set comprehension
a={b for b in range(1,11) if b%2!=0 }
print(a)
a={b for b in range(1,11) if b%2==0 }
print(a)
# union
x={1,2,3,4,5}
y={5,6,7,8}
print(x.union(y))
print(x|y)
# intersection
print(x-y)
print(y-x)
# difference
print(x&y)

# index value in set '[]' brackets: set is a unordered collection of unique elements.
# s={10,20,30,40}
# print ([s[0]) makes error? becz set object is not subscriptable.
