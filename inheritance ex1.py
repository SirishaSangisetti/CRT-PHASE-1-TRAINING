class Bankmanager:
    account_info="two"
    withdraw =False
class employee(Bankmanager):
    cash="lakh"
    accountno = 121537
class accountholder(employee):
    withdraw=True
    accountno=3624828
obj=accountholder()
obj.account_info="one"
print(obj.accountno)
print(obj.withdraw)
print(obj.account_info)
print(obj.cash)



