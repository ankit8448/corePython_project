# # atm
import time
print('        WELCOME TO SBI        ')
print("_"*50)
time.sleep(2)
print("press 1 for debit")
print("press 2 for credit")
print("press 3 for balance inquery")
print("press 4 for exit")
time.sleep(2)
balance=10000
password=1363
while True:

    user=int(input('enter your chosen option:'))
    time.sleep(2)

    if user==1:
        limit = 5
        while limit>=1:
            limit-=1
            pin=int(input('enter your pin here :'))
            time.sleep(2)
            if pin==password:
                print("corect pin")
                break
            print("wrong pin ,try again")
            print("-"*50)
            print("attempts left :",limit)
            print("you have used all your trials , now your pass is block:")
        
        amount=int(input("enter amount you want to withdraw:-"))
        balance-=amount
        time.sleep(1)
        print("amount",amount,"withdrawl successfully")
        print("-"*50)
        time.sleep(2)
        print("balance :-",balance)
    elif user==2:
        limit = 5
        while limit>=1:
            limit-=1
            pin=int(input('enter your pin here :'))
            time.sleep(2)
            if pin==password:
                print("corect pin")
                break
            print(" wrong pin ,try again")
            print("-"*50)
            print("attempts left :",limit)
            print("you have used all your trials , now your pass is block:")
        amount=int(input("enter amount you want to deposit:-"))
        balance+=amount
        time.sleep(1)
        print("amount of ",amount,"deposited successfully")
        print("-"*50)
        time.sleep(2)
        print("balance :-",balance)
    elif user==3:
        limit = 5
        while limit>=1:
            limit-=1
            pin=int(input('enter your pin here :'))
            time.sleep(2)
            if pin==password:
                print("corect pin")
                break
            print(" wrong pin ,try again")
            print("-"*50)
            print("attempts left :",limit)
            print("you have used all your trials , now your pass is block:")
        print("fetching.....")
        print("-"*50)
        time.sleep(1)
        print("your balance is :",balance)
    else :
        print("choose correct option!")










