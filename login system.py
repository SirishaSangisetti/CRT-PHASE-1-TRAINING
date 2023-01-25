class userclass:
    full_name=""
    email=""
    __password=""
    mobile_no=""
    def __init__(self,name,email,password):
        self.full_name=name
        self.email=email
    def update_name(self,new_name):
        self.update_name=new_name
        def get_name(self):
            return self.full_name
        def update_password(self,new_password):
            self.__password=new_password
        def update_mobile_no(self,new_number):
            self.mobile_no= new_number
        def get_user_password(self):
            return self.__password

