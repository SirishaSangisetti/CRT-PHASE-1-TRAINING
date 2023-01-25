from user import userclass
class Login:
    __db=[]
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("welcome user")
        print("1.register")
        print("2.login")
        print("3.exit")
    def create_user(self,name,email,paswssword):
        new_user=userclass(name,email,password)
        self.__db.append(new_user)
        print(self.__db)
    def validate_user(self,email,password):
        pass
obj=Login()
while True:
    option=input("enter your choice")
    if option=='1':
        name=input("enter your full name:")
        email=input("enter email:")
        password=input("create new password:")
        res=obj.create_user(name,email,password)
        if res==True:
            print("created new user successfully")
    elif option=='2':
        pass
    elif option=='3':
        break
    else:
        print("invalid input")

