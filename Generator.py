#Generator:
def my_gen():
    yield 'A'
    yield 'B'
g=my_gen()
print(type(g))
print(next(g))
print(next(g))
# or
for i in g:
    print(i)

l=[]
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for i in fib():
    if i >=100:
        break
    print(i)