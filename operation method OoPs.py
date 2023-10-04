class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return (self.pages + other.pages)

b1=Book(100)
b2=Book(200)
print(b1+b2)
#------------------------------------------------------------------
class Assaignment:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self, other):
        return (self.marks + other.marks)
a1=Assaignment(95)
a2=Assaignment(87)
a3=Assaignment(76)
a4=Assaignment(35)
a5=Assaignment(68)
print(a1+a3)
# ---------------------------------------------------------------
class Calculation:
    def __init__(self,mark):
        self.mark=mark
    def __add__(self, other):
        return (self.mark+other.mark)
    def __sub__(self, other):
        return (self.mark-other.mark)
    def __mul__(self, other):
        return (self.mark*other.mark)
    def __truediv__(self, other):
        return (self.mark/other.mark)

a1=Calculation(66)
a2=Calculation(75)
a3=Calculation(5)
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a2/a3)
#---------------------------------------------------------------------
