class Rbi:
    def money(self):
        print("in crores")
class Sbi:
    def money(self):
        print("in lakhs")
class localbank(Rbi,Sbi):
    pass
obj=localbank()
obj.money
