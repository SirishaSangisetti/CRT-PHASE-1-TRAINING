#single--one parent onechild
#multilevel--one after another parent
#heirarchical--multiple children
#multiple--two parents--python only

#example
class A:
    pass
class B(A):
    pass

##single
class A:
    name=""
    age=10
class B(A):
    age=11
obj=B()
print(obj.name)
print(obj.age)#10 first check its own class
obj.name="rsm"#name will update

##multilevel
class A:
    name=""
    age=10
class B(A):
    age=11
class c(B):
obj=B()
print(obj.name)
print(obj.age)#10 first check its own class
obj.name="rsm"#name will update


