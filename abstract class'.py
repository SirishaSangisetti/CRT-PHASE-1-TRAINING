#abc is the abstract based class module
#ABC-class
# from abc import ABC
# class Student(ABC):
#     def write_exams(self):
#         pass
# class A(Student):
#
from abc import ABC,abstractmethod
class Area(ABC):#abstract class
    @abstractmethod
    def calculate_area(self):#abstract methods
        print("in calculate area")
class Square(Area):
    def calculate_area(self):
        print("in square method")
    def calculate_circle_area(self):#define every method which is present in main class
        pass
class Rectangle(Area):
    pass
obj=Square()
obj.calculate_area()
