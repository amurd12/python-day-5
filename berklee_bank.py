bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}

'''
Task: print welcome message
Name: welcome_message
Input: none
Side Effects (print/display): "Welcome to Berklee Bank"
Return: none
'''
def print_welcome():
    print("===== Welcome to Berklee Bank ====")

'''
Task: promt for username
Name: get_username
Input: none
Side Effects (print/display): promt "What is your name?"
Return: return the username
'''
def get_username():
    name = input("What is your name? ")
    return name

'''
Task: promt user for pin
Name: pin_number
Input: none
Side Effects (print/display): promt "What is your pin? "
Return: return pin 
'''
def get_pin():
    pin = input("What is your pin? ")
    return pin 

'''
Task: take name and see if there is a valid user. if not they faile 
Name: verify_identity
Input: username, pin
Side Effects (print/display): if they dont exixt print "acess denied"
Return: True i user exixts, False if not 
'''
def verify_identity(username, pin):
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        if pin == users_values.get("pin"):
            return True
    print("Access Denied for ", username, "with pin ", pin)
    return False

'''
Task: prints the options they can do and ask them which one they want 
Name: get_menu_choice
Input: None
Side Effects (print/display): prints "Do you want to depsit, withdraw, get balance or quit? (they type their answer)
Return: the string the user typed in 
'''
def get_menu_choice():
    choice = input("Do you want to... Deposit - Withdraw - Balance - Quit ")
    return choice

'''
Task: gets balance and prints it
Name: get_balance
Input: username
Side Effects (print/display): print the balance
Return: None
'''
def get_balance(username):
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        balance = users_values.get("balance")
        print("Your balance is: ", balance)

    return None

'''
Task: ask user how much they want to deposit and adds it to the balance
Name: deposit_money
Input: username
Side Effects (print/display): promt user for ammount to depsoit 
Return: None
'''
def deposit_money(username):
    deposit_ammount = int(input("How much would you like to deposit? "))
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        previous_balance = users_values.get("Balance")
        new_balance = previous_balance + deposit_ammount 
        users_values.update({"balance": new_balance}) 

    return None

'''
Task: ask user how much they want to withdraw and if they have enough reduce the balance if not tell they they can't
Name: withdraw_money 
Input: username
Side Effects (print/display): asking user for ammout and tell them if it is sucessful or not 
Return: None
'''
def withdraw_money(username):
    withdraw_ammount = int(input("How much money would you like to withdraw? "))
    if bank_dict.get(username):
            users_values = bank_dict.get(username)
            previous_balance = users_values.get("balance")
            new_balance = previous_balance - withdraw_ammount
            if new_balance <0:
                print("Isufficent funds")
            else:
                users_values.update({"balance", new_balance})
         

def run_tests():
    withdraw_money("Priya") #Ask for ammount, if 200 fail
    withdraw_money("Priya") #Ask for ammount, if 100 should pass

    deposit_money("Priya") #Ask for ammount, if 100 should pass

    get_balance("Priya") # should print $100

    verify_identity("Priya", "4821") # Expecting login to work
    verify_identity("Priya", "5678") # Expecting login to fail


def main(): 
    print_welcome()
    name = get_username
    pin = get_pin
    valid = verify_identity(name, pin)   
    if not valid:
        return
    
    while True:
        users_choice = get_menu_choice()
        if users_choice == "balance":
            get_balance(name)

        elif users_choice == "deposit":
            deposit_money(name)

        elif users_choice == "deposit":
            deposit_money(name)

        else: 
            print("You can't choose that...")
        

main()
