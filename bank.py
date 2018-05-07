
#def personal_info(self,first_name,last_name,middle_name,account_type,balance,status):
#    self.first_name = first_name
#    self.last_name = last_name
#    self.middle_name = middle_name
#    self.account_type = account_type
#    self.balance = balance
#    self.status = status

balance = 0


def open_new_account():
    potential_account = input("would you like to open a new account? (y/n) ")
    if potential_account == "y":
        account_type()
    elif potential_account == "n":
        user_action = input("choose from one of the following: 1 to make a transfer, 2 to make a withdrawl, 3 to make a deposit: ")
        if user_action == "1":
            transfer()
        elif user_action == "2":
            withdrawl()
        elif user_action == "3":
            deposit()
        else:
            print("Error, invalid selection!")
            open_new_account()
    else:
        print("Thanks for coming in! ")
def account_type():
    type_of_account = input("What type of account would you like to open? press '1' for checking or '2' for savings: ")
    if type_of_account == "1":
        print("You chose checking! ")
        account_info()
    elif type_of_account == "2":
        print("You chose savings! ")
        account_info()
    else:
        print("invalid entry, try again")
        account_type()
    starting_balance = float(input("Initial deposit must be over $100. please enter amount of deposit: $"))
    if starting_balance > 99:
        print("Great, thank you!")
    else:
        print("Sorry, insufficient funds!")
def account_info():
    print("Now, lets get some personal info from you")
    first_name = input("Enter first name: ")
    middle_initial = input("Enter middle initial: ")
    last_name = input("Enter Last name: ")
def transfer():
    amount_to_transfer = float(input("how much would you like to transfer? $"))
    to_account = input("select an account to transfer 'to'. for savings press 1, for checking press 2: ")
    if to_account == "1":
        to_account = "savings"
        from_account = "checking"
    elif to_account == "2":
        to_account = "checking"
        from_account = "savings"
    print(f"You are transferring ${amount_to_transfer} from {from_account} to {to_account}")
    
def withdrawl():
    amount_to_withdrawal = float(input("How much would you like to take out? $"))
    new_balance = balance - amount_to_withdrawal
    print(f"Your remaining balance is {new_balance}")
def deposit():
    amount_to_deposit = float(input("How much would you like to deposit today? $"))
    new_balance = balance + amount_to_deposit
    print(f"Your new balance is ${new_balance}")
#class transfer:
#    def __init__(self,account_from,account_to,amount):
#        self.account_from = account_from
#        self.account_to = account_to
#        self.amount = amount
#
       # transfer = input("Select an account you'd like to transfer funds from: (checking/saving)")
