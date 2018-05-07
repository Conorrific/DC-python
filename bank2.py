import bank
welcome_message = input("Welcome to CB bank! press 1 to begin. To exit, press 'x': ")
if welcome_message == "1":
    bank.open_new_account()
elif welcome_message == "x":
    print("Have a great day!")
else:
    print("Invalid response, please try again!")
