# #  Multiple inheritance
class Father:
    def __init__(self,face):
        self.face=face
    def f1 (self):
        print('my face look like father face')
class Mother:
    def __init__(self,behaviour):
        self.behaviour=behaviour
    def f2 (self):
        print('i have my moms behaviour')
class Child (Father,Mother):
    def __init__(self,face,behaviour,hobby):
        Father.__init__(self,face)
        Mother.__init__(self,behaviour)
        self.hobby=hobby
    def f3 (self):
        print('my hobby is different from my parents')
c=Child('round','good','play')
c.f2()
c.f3()
# -----------------------------------------------------------------------------------
# # multi level inheritance
class Father:
    def __init__(self,salary):
        self.salary=salary
    def m1 (self):
        print('salary')
class Mother(Father):
    def __init__(self,salary,food):
        super().__init__(salary)
        self.food=food
    def m2 (self):
        print('food')
class Daughter (Mother):
    def __init__(self,salary,food,education):
        super().__init__(salary,food)
        self.education=education
    def m3 (self):
        print('education')

c=Daughter (1000,'dosa','high school')
c.m1()
c.m2()
# -----------------------------------------------------------------------------------

