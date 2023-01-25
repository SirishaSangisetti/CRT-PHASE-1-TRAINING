#any two  or more inheritances
class college:
    name="anything"
    establishement=1990
    type="government"
class engineering(college):
    name="pragati"
    branches="10"
    span="4"
    affliated_to=""
class degree(college):
    name="aditya"
    branches="15"
    span="3"
class under_maintanance(engineering,college):
    pass
obj=under_maintanance()
print(obj.name)
print(obj.branches)
print(obj.type)
