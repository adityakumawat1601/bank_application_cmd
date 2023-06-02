from getpass import getpass
import json
import os
import time

last_account = 1000
with open("last_account.json","w") as file:
    json.dump(last_account,file)

def last_account():
    with open("last_account.json","r") as file:
        last = json.load(file)
    return last

def make_new_account(last,details):
    new = last + 1
    with open(f"{new}","w") as file:
        json.dump(details,file)

def get_new_account(last):
    new_acc = last+1
    return new_acc

def update_last_account(account):
    
    with open("last_account.json","w") as file:
        json.dump(account,file)


def signup():
    print("Please enter credentials to open a bank account.")
    name = input("Name: ").strip().lower()
    password = input("Password: ")
    balance = float(input("Balance: "))
    details = {
        "name":name,
        "password":password,
        "balance":balance
    }
    last_acc = last_account()
    account = get_new_account(last_acc)
    update_last_account(account)
    make_new_account(last_acc,details)
    
    
    print(f"Congratulations {name} ! your account has been opened with Pineapple bank of india")
    print(f"Opening balance \u20B9{balance}")
    print(f"your account number is {account}")
    
def load_data(account):
    with open(f"{account}","r") as file:
        data = json.load(file)
        return data


def login():
    account = int(input("enter account number: "))
    password = getpass("enter password: ")
    data = load_data(account)
    if password == data['password']:
        os.system('cls')
        sub_menu()
        while True:
            choice = input("enter your choice: ")
            if choice == "1":
                add_amount(account)
            elif choice == "2":
                withdraw_amount(account)
            elif choice =="3":
                check_amount(account)
            elif choice =="4":
                print("------happy banking with Pineapple Bank of Inda------")
                break
                
    else:
        print("Invalid Password! try again")
    

def update_details(account,data):
    with open(f"{account}","w") as file:
        json.dump(data,file)


def add_amount(account):
    money = float(input("enter amount to add: "))
    data = load_data(account)
    data["balance"] += money
    update_details(account,data)
    
    print(f"thankyou for depositing amount of \u20B9{money} \nyour updated balance is {load_data(account)['balance']}")
    

def withdraw_amount(account):
    withdraw = int(input("withdraw amount: "))
    data = load_data(account)
    
    if withdraw <= data["balance"]:
        data["balance"] -= withdraw
        update_details(account,data)
        
        print(f"\u20B9{withdraw} is debited from account no.{account}\nNow available balance is {load_data(account)['balance']}")
    else:
        print(f"your bank balance is only \u20B9{data['balance']}")
        print("please enter a valid amount to withdraw.")
    
def check_amount(account):
    print(f"your account balance in pineapple bank as per now is \u20B9{load_data(account)['balance']}.")
    print("Thankyou for using pineapple Bank")
    
def main_menu():
    main_menu = '''            WELCOME TO PINE-APPLE BANK
                               
               1. LOGIN
               2. SIGNUP
               3. EXIT
    
    '''
    os.system('cls')
    print(main_menu)
    ch = input("enter your choice: ")
    
    if ch == "1":
        login()
    elif ch == "2":
        signup()
    elif ch == "3":
        exit(0)
    else:
        print("Invalid option ! try again")


def sub_menu():
    sub_menu = '''  
                     1.Add amount
                     2.Withdraw amount
                     3. Check bank balance
                     4.logout
    '''
    
    print(sub_menu)
    
#---------------------------------------------------------------------------
if __name__ == "__main__":
    while True:
        main_menu()
        input("press enter to continue: ")