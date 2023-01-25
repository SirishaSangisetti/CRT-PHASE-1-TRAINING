
f="a"
age=30
l="years of old"
print(f+ str(age)+l)

print("a is  {} years old".format(age))

###
num=4
print("square of {} is {}".format(num,num*num))
print(f"square of {num} is {num*num:.5f}")
print(f"square of {num} is {num*num}")
print("square of {} is {:.2f}".format(num,num*num))#gives 2 num after decimal
######
a=int(input('enter a: '))
b=int(input('enter b: '))
print(a/b)

###expetion hadling
a=int(input('enter a: '))
b=int(input('enter b: '))
try:
    print(a/b)
except:
    print("b cant be zero")
    print("after the error")

