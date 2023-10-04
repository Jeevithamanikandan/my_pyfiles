from abc import *
class Fruit(ABC):
    @abstractmethod
    def tast (self):
        pass
f=Fruit()
f.tast()

from abc import *
class Vehicle (ABC):
    @abstractmethod
    def noofwheels(self):
        pass
class Bus(Vehicle):
    pass
f=Bus()
# -----------------------------------------------------------------------------------
from abc import *
class Vehicle (ABC):
    @abstractmethod
    def noofwheels(self):
        pass
class Bus(Vehicle):
    def noofwheels(self):
        # print('there are 7 wheels')
        return 7
class Minivan (Bus):
    def noofwheels(self):
        return 4
        # print('4 weels')

f=Bus()
f1=Minivan()
print(f.noofwheels())
print(f1.noofwheels())
# -----------------------------------------------------------------------------------
# private, protected, public
class Test:
    x=10
    _y=20
    __z=30
    def m1 (self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)
t=Test()
t.m1()
print(Test.x)
print(Test._y)
print(t._Test__z)

