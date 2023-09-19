# [Has a method in inheritance ]
# (example 1)
# class Engine:
#     a=10
#     def __init__(self):
#         self.b=20
#     def m1 (self):
#         print('Engine specification')
# class Car:
#     def __init__(self):
#         self.engine=Engine()
#     def m2 (self):
#         print('car using clay function')
#         print(self.engine.a)
#         print(self.engine.b)
#         self.engine.m1()
# c=Car()
# c.m2()

# excercise
# class Geography:
#     features=3
#     def __init__(self):
#         self.instrument='rotometer'
#         self.reference='toposheet'
#         self.material='tracing sheet'
#     def m1 (self):
#         print('Geography department features')
# class Geospatial:
#     def __init__(self):
#         self.geography=Geography()
#     def m2 (self):
#         print(self.geography.instrument,self.geography.reference,self.geography.material)
#         self.geography.m1()
# a=Geospatial()
# a.m2()