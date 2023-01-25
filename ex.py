
def invert(string):
    res=""
    for i in string:
        if i==0:
            res+=1
        else:
            res+=0
        return res
a=int(input())
b=int(input())
new_a=bin(a)[2:]
new_b=bin(a)[2:]
new_a=invert(new_a)
new_b=invert(new_b)
x=(int(new_a,2))
y=(int(new_b,2))
print(x^y)



