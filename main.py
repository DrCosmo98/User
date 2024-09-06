from account_handler import account_handler

ah = account_handler()
ah.password()

while True:
    reg_status = input('enter the following "l" or "s" or "exit" \n') 
    
    if reg_status == "s":
        
        ah.enter_username()
        while True:
           if ah.enter_password() == True:
               break
    elif reg_status == "l":
        while True:
            if ah.check_username() == True:
                break
        ah.check_password()
        print(ah.username + " logged in")
    elif reg_status == "exit":
        exit()
    
    else:
        print("Invalid option. Try again. \n")