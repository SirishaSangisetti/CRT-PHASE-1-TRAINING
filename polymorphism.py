# def m1(a,b):
#     print(a,b)
# def m1(a,b,c):
#     print(a*b*c)
# print(m1(10,20))#error  #same method different signatures==method overloading

class A:
    def m1(self):
        print("in class A")
class B(A): #different classes same method
    def m1(self):
        print("in class B")
obj=B()

