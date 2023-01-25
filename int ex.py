for i in range(5):
    try:
        int(input())
    except:
        print("cant be string")

###
try:
    arr=list(map(int,input(.split(' '))))
except:
    print("enter intrger input")

    ##
    print(eval("1+3/5*9"))