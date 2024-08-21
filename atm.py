username="Hemanth"
password ='HemanthH@123'
c_name=input("Enter your name:")
c_pass=str(input("Enter your password:"))

if c_name==username and c_pass==password:
    print('''
    1.Deposite
    2.Withdraw
    3.Ministatement
    4.Exit
          ''')
    amount=50000
    option = int(input("select your options:"))
    if option==1:
        dep=int(input("Enter the amount:"))
        amount+=dep 
        print("Total amount:",amount)
    elif option==2:
        withdraw_amount=int(input("Enter the amount:"))
        amount-=withdraw_amount
        print("Remaining amount:",amount)
    elif option==3:
        print("======ATM======")
        print("Username:",username)
        print("Total amount:",amount)
        print("Thanks for visiting")
        print("======ATM======")
    elif option==4:
        exit()
else:
    print("Please Enter Correct Logins")