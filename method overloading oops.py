#over loading
#
class Test:
    def m1 (self):
        print('no-arguments')
    def m1 (self,a):
        print('one argument')
    def m1 (self,a,b):
        print('2 argument')
t= Test()
t.m1(10,20)
# -----------------------------------------------------------------------------------
#
# class Test:
    def m1 (self):
        print('no-arguments')
    def m1 (self,a,b):
        print('2 argument')
    def m1 (self,a):
        print('1 argument')
t= Test()
t.m1(10)
# -----------------------------------------------------------------------------------
# here we can control over loading method
class Test:
    def sum (self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('sum',a+b+c)
        elif a!=None and b!=None:
            print('sum',a+b)
        else:
            print('please give 1 or 2 arguments')
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
# -----------------------------------------------------------------------------------
# over riding method
class P:
    def property (self):
        print('gold+land+cash')
    def marry (self):
        print('arrange marrage')
class C(P):
    def marry (self):
        print('love marrage')
c=C()
c.property()
c.marry()
# -----------------------------------------------------------------------------------

class P:
    def property (self):
        print('gold+land+cash')
    def marry (self):
        print('arrange marrage')
class C (P):
    def marry (self):
        super().marry()
        print('love marrage')
c=C()
c.property()
c.marry()
# -----------------------------------------------------------------------------------
class Father:
    def hobby (self):
        print('making craft')
    def behaviour (self):
        print('silent')
    def always (self):
        print('happy')
class Jeevitha(Father):
    def behaviour(self):
        print('stiching')
    def always(self):
        print('sad')
c=Jeevitha()
c.hobby()
c.behaviour()
c.always()
