
db=[{'Q8@ex.com':'1234'},
   {'q9@ex.com':'5678'},
   {'q1@ex.com':'3456'},
   {'q2@ex.com':'56778'}
   ]
print(db)
username=input("enter username")
password=input("enter password")
temp={
    username:password
}

if temp in db:
    print("found")
else:
    print("not found")

    if(db[i]==input()):
        print("login successfully")