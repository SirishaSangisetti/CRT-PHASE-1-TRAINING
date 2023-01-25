class p1:
    def m1(self):
        print("in parent 1")
class p2:
    def m1(self):
        print("in parent 2")
class c(p1,p2):#diamond problem--chilld class accessimg method which is present
                 # in both the parents occurimg error
    pass
obj=c()
obj.m1()
#gives the method which was first called
