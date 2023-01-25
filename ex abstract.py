from abc import ABC,abstractmethod
class Student(ABC):
    @abstractmethod
    def write_exams(self):
        print("schedule")
    def result(self):
        print("yet to release")
class second_year(Student):
    def write_exams(self):
        print(" not completed")
    def result(self):
        print("yet to be release")
class third_year(Student):
    def write_exams(self):
        print("completed")
    def result(self):
        pass
obj=third_year()
print(obj.result())
print(obj.write_exams())


