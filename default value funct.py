#normal
def add(n1,n2):
    return n1+n2
a=1
b=2
res=add(a,b)
res=add(a)#error
res=add(a,b,c)#error
print(res)

## default
def add(n1,n2=0):
    return n1+n2
a=1
b=2
res=add(a)
print(res)

##keyword
def add(n1,n2):
    print("n1:",n1)
    a=10
    b=20
add(n2=10,n1=20)


#first give keyword arguments and positional are not same