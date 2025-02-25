#Buidling A Simple ATM System
PIN = "1234"
balance =[1000]
min_bal=[200]
history=[]

print("Welcome to STS Bank\nYour Money is Secured")

def welcome_page(PIN):
    attempt = 3
    while attempt !=0:
        attempt= attempt -1
        pin= input("\nEnter Your 4 digit pin to continue:")
        
        if  attempt >=1 and pin != PIN :           
            print(f"\nIncorrect Pin. You Have {attempt} More Attempt")
        elif attempt == 0 and pin != PIN:
            print("\nToo Many Incorrect Attempts")
        else:
            break
    else:
        print("Your Card Has Been Blocked. Contact STS Bank")
    

def check_balance():
    print(f"\nYour Available Balance is:USD {balance[0]:,.2f}")
    
def make_deposit():
    try:
        dep_amount= float(input("\nEnter deposit amount:"))
    except:
        print("Invalid Amount. Please Enter a Valid Amount")
        quit()
        
    if dep_amount <= 0:
        print("\nWrong Input, Please Enter Amount to Deposit")
    else:
        
        balance[0]= balance[0] + (dep_amount)
        history.append(f"Deposit - USD {dep_amount:,.2f}")
        print(f"\nDeposit of USD {dep_amount:,.2f} Successful\n")
        print(f"Your Available Balance is: USD {balance[0]:,.2f}\n")
        return balance

def cash_withdraw():
    try:
        amount_wd= float(input("\nEnter Amount To Withdraw:"))
    except:
        print("Invalid Amount. Please Enter a Valid Amount")
        
        
    if balance[0]<amount_wd:
        print("Insufficient Balance\n")
    elif (balance[0]-amount_wd)<=min_bal[0]:
        print("Insufficient Balance\n")
    elif amount_wd>4000:
        print("Max Withdrawal of 4,000.00 Allowed.\nEnter Amount (1-4000)")
    elif amount_wd<= 0:
        print("Wrong Amount Entered. Please Enter Amount To Withdraw\n")
    else:
        balance[0] = balance[0] - int(amount_wd)
        history.append(f"Withdrawal- USD {amount_wd:,.2f}")
        print(f"\nWithdrawal of USD {amount_wd:,.2f} Successful\n")
        print(f"Available Balance is USD {balance[0]:,.2f} \n")
        return balance

def transact_history():
    print("\nTransaction History")
    if len(history)<1:
        print("No Transactions To View")
    for items in history:
        print(items)

def main():
    welcome_page(PIN)
    
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. View Transaction History")
        print("5. Exit") 
        choice =input("\nEnter Your Action:")
        
        if choice == "1":
            check_balance()
        elif choice == "2":
           balance = make_deposit()
        elif choice == "3":
           balance= cash_withdraw()
        elif choice == "4":
            transact_history()
        elif choice == "5":
            print("Thank You For Banking With STS Bank\nPlease Remove Your ATM Card\n")
            break
        else:
            print("\nEnter A Numeric Input(1-5)")

if __name__=="__main__":
    main()