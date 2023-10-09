# Decorator:
def decorator (func):
    def inside (name):
        if name=='Praveen':
            print('hey praveen your good in your job ')
        else:
            print('you have to put some extra efferts')
    return inside
@decorator
def wish(name):
    print('hello',name,'good morning')
wish('Jeevitha')
wish('Praveen')
wish('Samyuktha')
# ------------------------------------------------------------------------
def decorator (func):
    def inner (a,b):
        if b==0:
            print('how can you divide by 0')
        else:
            func(a,b)
    return inner
@decorator
def sum (a,b):
    c=a/b
    print(c)
sum(10,2)
sum(2,0)

