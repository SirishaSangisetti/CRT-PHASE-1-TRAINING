l=[1,2,3,4]
a=2
temp=False
for i in range(len(l)):
    if a==l[i]:
        temp=True
        break
if temp==False:
    print("element not found")