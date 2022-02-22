print()
print("Welcome to BNC Bank: ")
print()
Username = "Will"

# Authentication level 1
class UsernameAndPassword():
    while True:
        username = input("Please type your created username: ")
        if username == "Will":
            print()
            print("Username Accepted")
            break
        else:
            print()
            print("Username Denied")
            print()
    print()
    while True:
        password = input("Please type your created password: ")
        if password == "1234":  
            print()
            print("Password Accepted")
            print()
            break
        else:
            print()
            print("Password Denied")
            print()
    print()

# Authentication level 2
# The pin number is based off of value not index
class PinNumber():
    while True:
        pin = int(input("Please choose a 4 digit Pin Number for your BNC Bank Account: "))
        print()
        if pin in range(0,10000):
            print()
            print("Pin Number Accepted")
            print()
            break
        else:
            print("Pin number invalid")   
            print()
    print()

# Ability to recreate pin number

    if pin in range(-10,-1) or pin in range(10000,50000):
        pin = int(input("Recreate Pin Number: "))
        print()
        print("Pin number invalid")
    print()

# States

class checking_Account():
    def __init__(self,account):
        self.account = account
    def account_Balance(self, balance):
        self.balance = balance
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account Balance has been updated: $", self.balance)
    def withdraw(self, amount):
        self.amount = amount
        if amount > self.balance:
            print("Insufficeint funds | Available Balance: $ ", self.balance)
        else:
            self.balance - amount
            print(f'{Username} `s Account has been updated: $', self.balance)
    def view_Balance(self, balance):
        self.balance = balance
        print(f'{Username} `s Account Balance is: $', self.balance)

class main():
    welcome = input("Welcome to " f'{Username}''`s' " Bnc Bank Account. Would you like to access your BNC Bank checking account? (Type (y)es or (n)o): ")
    my_account = checking_Account
    print()
    my_account.account_Balance = 0
    print() 
    if welcome == "yes" or welcome == 'Yes'or welcome == 'YES' or welcome == 'Y' or welcome == 'y':
        print("Available account balance: $", my_account.account_Balance)
        print()
    else:
        print()
        print(f"Now Leaving {Username}`s BNC Bank Account")
        quit()

# Behaviors

class TransactionClass():
    while True:
        my_account = checking_Account
        # Trial 1
        Transaction = input("Would you like to make a transaction? (Type (y)es or (n)o): " )
        print()
        if  Transaction == "yes" or Transaction == 'Yes' or Transaction == 'YES' or Transaction == "y":
            class choose_The_Transaction_Type():
                    my_account = checking_Account
                    choose_Transaction_Type = input("Would you like to (d)eposit, (w)ithdraw, or (v)iew balance?): ")
                    print()
                    if  choose_Transaction_Type == "deposit" or choose_Transaction_Type == "d": 
                        print()               
                        deposit = int(input("How much money would you like to deposit?: $"))
                        print()
                        my_account.account_Balance = my_account.account_Balance + deposit
                        print()
                        print("Your Updated Balance is: $",my_account.account_Balance)
                        print()
                    if  choose_Transaction_Type == "withdraw" or choose_Transaction_Type == "w":
                        withdrawl = int(input("How much money would you like to withdraw?: $"))
                        print()
                        if withdrawl > my_account.account_Balance:
                            print("Insufficent Funds | Available balance: $", my_account.account_Balance)
                            pass
                            print()           
                        else:
                            my_account.account_Balance = my_account.account_Balance - withdrawl
                            print("Your Updated Balance is: $",my_account.account_Balance)
                            print()
                    if  choose_Transaction_Type == "view balance" or choose_Transaction_Type == "vb" or choose_Transaction_Type == "v":
                        my_account.account_Balance == my_account.view_Balance
                        print(f'{Username}`s Available Balance: $',my_account.account_Balance)
                        print()
            break
        if Transaction == 'no' or Transaction == 'No'or Transaction == 'NO' or Transaction == 'n' or Transaction == 'N':
            print(f'Thank you for choosing BNC Bank. Now Leaving {Username}`s Bnc Bank Account!')
            quit()
        else:
            print()
            print("Sorry, invalid input. Please Try again")
            print()
        # Trial 2
        Transaction = input("Would you like to make a transaction? (Type (y)es or (n)o): " )
        print()
        if  Transaction == "yes" or Transaction == 'Yes' or Transaction == 'YES' or Transaction == "y":
            class choose_The_Transaction_Type():
                    my_account = checking_Account
                    choose_Transaction_Type = input("Would you like to (d)eposit, (w)ithdraw, or (v)iew balance?): ")
                    print()
                    if  choose_Transaction_Type == "deposit" or choose_Transaction_Type == "d": 
                        print()               
                        deposit = int(input("How much money would you like to deposit?: $"))
                        print()
                        my_account.account_Balance = my_account.account_Balance + deposit
                        print()
                        print("Your Updated Balance is: $",my_account.account_Balance)
                        print()
                    if  choose_Transaction_Type == "withdraw" or choose_Transaction_Type == "w":
                        withdrawl = int(input("How much money would you like to withdraw?: $"))
                        print()
                        if withdrawl > my_account.account_Balance:
                            print("Insufficent Funds | Available balance: $", my_account.account_Balance)
                            pass
                            print()           
                        else:
                            my_account.account_Balance = my_account.account_Balance - withdrawl
                            print("Your Updated Balance is: $",my_account.account_Balance)
                            print()
                    if  choose_Transaction_Type == "view balance" or choose_Transaction_Type == "vb" or choose_Transaction_Type == "v":
                        my_account.account_Balance == my_account.view_Balance
                        print(f'{Username}`s Available Balance: $',my_account.account_Balance)
                        print()
            break
        if Transaction == 'no' or Transaction == 'No'or Transaction == 'NO' or Transaction == 'n' or Transaction == 'N':
            print(f'Thank you for choosing BNC Bank. Now Leaving {Username}`s Bnc Bank Account!')
            quit()
        else:
            print()
            print("Sorry, invalid input. Please Try again")
            print()
        # Trial 3
        Transaction = input("Would you like to make a transaction? (Type (y)es or (n)o): " )
        print()
        if  Transaction == "yes" or Transaction == 'Yes' or Transaction == 'YES' or Transaction == "y":
            class choose_The_Transaction_Type():
                    my_account = checking_Account
                    choose_Transaction_Type = input("Would you like to (d)eposit, (w)ithdraw, or (v)iew balance?): ")
                    print()
                    if  choose_Transaction_Type == "deposit" or choose_Transaction_Type == "d": 
                        print()               
                        deposit = int(input("How much money would you like to deposit?: $"))
                        print()
                        my_account.account_Balance = my_account.account_Balance + deposit
                        print()
                        print("Your Updated Balance is: $",my_account.account_Balance)
                        print()
                    if  choose_Transaction_Type == "withdraw" or choose_Transaction_Type == "w":
                        withdrawl = int(input("How much money would you like to withdraw?: $"))
                        print()
                        if withdrawl > my_account.account_Balance:
                            print("Insufficent Funds | Available balance: $", my_account.account_Balance)
                            pass
                            print()           
                        else:
                            my_account.account_Balance = my_account.account_Balance - withdrawl
                            print("Your Updated Balance is: $",my_account.account_Balance)
                            print()
                    if  choose_Transaction_Type == "view balance" or choose_Transaction_Type == "vb" or choose_Transaction_Type == "v":
                        my_account.account_Balance == my_account.view_Balance
                        print(f'{Username}`s Available Balance: $',my_account.account_Balance)
                        print()
            break
        if Transaction == 'no' or Transaction == 'No'or Transaction == 'NO' or Transaction == 'n' or Transaction == 'N':
            print(f'Thank you for choosing BNC Bank. Now Leaving {Username}`s Bnc Bank Account!')
            quit()
        else:
            print()
            print("Sorry, invalid input. Please Try again")
            print()
        break

                                
            
                    
                        
        
class AnotherTransaction():
    while True:
        # Trial 1           
        another_Transaction = input("Would you like to make another transaction? (Type (y)es or (n)o): " )
        print()
        if  another_Transaction == 'yes'or another_Transaction == 'Yes' or another_Transaction == 'YES' or another_Transaction == "y" or another_Transaction == 'Y':
            class choose_Another_Transaction_Type():
                    my_account = checking_Account
                    choose_Transaction_Type = input("Would you like to (d)eposit, (w)ithdraw, or (v)iew balance?): ")
                    print()
                    if  choose_Transaction_Type == "deposit" or choose_Transaction_Type == "d": 
                        print()               
                        deposit = int(input("How much money would you like to deposit?: $"))
                        print()
                        my_account.account_Balance = my_account.account_Balance + deposit
                        print()
                        print("Your Updated Balance is: $",my_account.account_Balance)
                        print()
                    if  choose_Transaction_Type == "withdraw" or choose_Transaction_Type == "w":
                        withdrawl = int(input("How much money would you like to withdraw?: $"))
                        print()
                        if withdrawl > my_account.account_Balance:
                            print("Insufficent Funds | Available balance: $", my_account.account_Balance)
                            pass
                            print()           
                        else:
                            my_account.account_Balance = my_account.account_Balance - withdrawl
                            print("Your Updated Balance is: $",my_account.account_Balance)
                            print()
                    if  choose_Transaction_Type == "view balance" or choose_Transaction_Type == "vb" or choose_Transaction_Type == "v":
                        my_account.account_Balance == my_account.view_Balance
                        print(f'{Username}`s Available Balance: $',my_account.account_Balance)
                        print()

            continue
        if another_Transaction == 'no' or another_Transaction == 'No'or another_Transaction == 'NO' or another_Transaction == 'n' or another_Transaction == 'N':
            print()
            print(f'Thank you for choosing BNC Bank. Now Leaving {Username}`s Bnc Bank Account!')
            quit()
        else:
            print()
            print("Sorry, invalid input. Please Try again")
            print()
            # Trial 2
        another_Transaction = input("Would you like to make another transaction? (Type (y)es or (n)o): " )
        print()
        if  another_Transaction == 'yes'or another_Transaction == 'Yes' or another_Transaction == 'YES' or another_Transaction == "y" or another_Transaction == 'Y':
            class choose_Another_Transaction_Type():
                    my_account = checking_Account
                    choose_Transaction_Type = input("Would you like to (d)eposit, (w)ithdraw, or (v)iew balance?): ")
                    print()
                    if  choose_Transaction_Type == "deposit" or choose_Transaction_Type == "d": 
                        print()               
                        deposit = int(input("How much money would you like to deposit?: $"))
                        print()
                        my_account.account_Balance = my_account.account_Balance + deposit
                        print()
                        print("Your Updated Balance is: $",my_account.account_Balance)
                        print()
                    if  choose_Transaction_Type == "withdraw" or choose_Transaction_Type == "w":
                        withdrawl = int(input("How much money would you like to withdraw?: $"))
                        print()
                        if withdrawl > my_account.account_Balance:
                            print("Insufficent Funds | Available balance: $", my_account.account_Balance)
                            pass
                            print()           
                        else:
                            my_account.account_Balance = my_account.account_Balance - withdrawl
                            print("Your Updated Balance is: $",my_account.account_Balance)
                            print()

                    if  choose_Transaction_Type == "view balance" or choose_Transaction_Type == "vb" or choose_Transaction_Type == "v":
                        my_account.account_Balance == my_account.view_Balance
                        print(f'{Username}`s Available Balance: $',my_account.account_Balance)
                        print()
            continue
        if another_Transaction == 'no' or another_Transaction == 'No'or another_Transaction == 'NO' or another_Transaction == 'n' or another_Transaction == 'N':
            print()
            print(f'Thank you for choosing BNC Bank. Now Leaving {Username}`s Bnc Bank Account!')
            quit()
        else:
            print()
            print("Sorry, invalid input. Please Try again")
            print()
        # Trial 3
            another_Transaction = input("Would you like to make another transaction? (Type (y)es or (n)o): " )
            print()
            if  another_Transaction == 'yes'or another_Transaction == 'Yes' or another_Transaction == 'YES' or another_Transaction == "y" or another_Transaction == 'Y':
                class choose_Another_Transaction_Type():
                    my_account = checking_Account
                    choose_Transaction_Type = input("Would you like to (d)eposit, (w)ithdraw, or (v)iew balance?): ")
                    print()
                    if  choose_Transaction_Type == "deposit" or choose_Transaction_Type == "d": 
                        print()               
                        deposit = int(input("How much money would you like to deposit?: $"))
                        print()
                        my_account.account_Balance = my_account.account_Balance + deposit
                        print()
                        print("Your Updated Balance is: $",my_account.account_Balance)
                        print()
                    if  choose_Transaction_Type == "withdraw" or choose_Transaction_Type == "w":
                        withdrawl = int(input("How much money would you like to withdraw?: $"))
                        print()
                        if withdrawl > my_account.account_Balance:
                            print("Insufficent Funds | Available balance: $", my_account.account_Balance)
                            pass
                            print()           
                        else:
                            my_account.account_Balance = my_account.account_Balance - withdrawl
                            print("Your Updated Balance is: $",my_account.account_Balance)
                            print()
                    if  choose_Transaction_Type == "view balance" or choose_Transaction_Type == "vb" or choose_Transaction_Type == "v":
                        my_account.account_Balance == my_account.view_Balance
                        print(f'{Username}`s Available Balance: $',my_account.account_Balance)
                        print()
                continue
            if another_Transaction == 'no' or another_Transaction == 'No'or another_Transaction == 'NO' or another_Transaction == 'n' or another_Transaction == 'N':
                print(f'Thank you for choosing BNC Bank. Now Leaving {Username}`s Bnc Bank Account!')
                quit()
            else:
                print()
                print("Sorry, invalid input. Please Try again")
                print()



        
    
        
        
        
            
       
                
        
                  





        
    





        















        












                        
                        



            


        



