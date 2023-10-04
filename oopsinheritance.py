# multiple inheritance:
class P1:
    def m1 (self):
        print('parent class')
class P2:
    def m1 (self):
        print('parent2 class')
class C (P1,P2):
    def m2 (self):
        print('child method')
c=C()
c.m1()
c.m2()
# -----------------------------------------------------------------------------------
# calling method using super method:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def method1 (self):
        print('hello')
class Employe(Person):
    def m2(self):
        super().method1()

c=Employe('jeevitha',21)
c.m2()
# -----------------------------------------------------------------------------------
# multiple inheritance excercise:
class Family1():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1 (self):
        print('we are first generation people')
class Family2():
    def __init__(self,doughter,son):
        self.doughter=doughter
        self.son=son
    def m1 (self):
        print('we are second generation')
class Child(Family2,Family1):
    def __init__(self,salary):
        super().__init__(Family2,Family1)
        self.salary=salary
    def m3 (self):
        print('i am third generation')
a=Child('jeevitha','sabaree',)
a.m1()
a.m3()
# -----------------------------------------------------------------------------------
# class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1 (self):
        print('ear briyani and drink water')
class Employe(Person):
    def __init__(self,name,age,no,salary):
        super(). __init__(name,age)
        self.no=no
        self.salry=salary
    def __str__(self):
        return 'name={},age={},no={},salary={}'.format(self.name,self.age,self.no,self.salry)
jeevitha=Employe('jeevitha',21,1,1000000)
print(jeevitha)
# -----------------------------------------------------------------------------------
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1 (self):
        print('hi,how are you')
class Student(Person):
    def __init__(self,name,age,no,mark):
        super().__init__(name,age)
        self.no=no
        self.mark=mark
    def m2 (self):
        print('work hard')
    def studentinfo(self):
        print('im',self.name)
        print('and im year old',self.age)
        print('mark',self.mark)
        print('no',self.no)
e=Student('jeevitha',21,2,99)
e.m1()
e.m2()
e.studentinfo()
# =========================================



