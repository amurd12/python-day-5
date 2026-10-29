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

'''
Task: promt for username
Name: get_username
Input: none
Side Effects (print/display): promt "What is your name?"
Return: return the username
'''

'''
Task: promt user for pin
Name: pin_number
Input: none
Side Effects (print/display): promt "What is your pin?"
Return: return pin 
'''

'''
Task: take name and see if there is a valid user. if not they faile 
Name: verify_identity
Input: username, pin
Side Effects (print/display): if they dont exixt print "acess denied"
Return: True i user exixts, False if not 
'''

'''
Task: prints the options they can do and ask them which one they want 
Name: get_menu_choice
Input: None
Side Effects (print/display): prints "Do you want to depsit, withdraw, get balance or quit? (they type their answer)
Return: the string the user typed in 
'''

'''
Task: gets balance and prints it
Name: get_balance
Input: username
Side Effects (print/display): print the balance
Return: None
'''

'''
Task: ask user how much they want to deposit and adds it to the balance
Name: deposit_money
Input: username
Side Effects (print/display): promt user for ammount to depsoit 
Return: None
'''

'''
Task: ask user how much they want to withdraw and if they have enough reduce the balance if not tell they they can't
Name: withdraw_money 
Input: username
Side Effects (print/display): asking user for ammout and tell them if it is sucessful or not 
Return: None
'''

