#define my global username and password variables
username = None
password = None

#method that asigns new username
def enter_username(new_username):
    global username # modifying the global variable
    username = new_username
    print(username + " is now your user name welcome \n")
    
    #doesnt need a return as there is no value to return as it is just setting the username
    
#method that asigns new password and verfiy 
def enter_password(new_password):
    global password # modifying the global variable

    #validtation of password
    while True:
        if len(new_password) > 8 and len(new_password) < 15:
            
            #set all checks to flase to start with
            lower_case = False
            upper_case = False
            num = False
            special = False
            
            # checking if it contains the following has at lease 1 number, upper, lower and special char            
            for char in new_password:
                if(char.isdigit()):
                    num = True
                if(char.islower()):
                    lower_case = True
                if(char.isupper()):
                    upper_case = True
                    
                # check if it has at least one char that is not a letter or num
                if(not char.isalnum()): 
                    special = True
            if lower_case and upper_case and num and special:#replaced the return statement to if statement as the return was ending the loop
                #assign the new_password as the global password
                password = new_password
                print(" your password is now set \n")
                
                #print for testing purposes
                print(password)
                return
            
            #this reloops to ask for a new input from the user
            
            else: 
                continue
                #do i really need this?
        else:
                new_password = input("password must contain, lower case, upper case, special character, number. must be between 8 - 15 characters. try again \n")
    
 #checks if user name is correct
def check_login(checked_login):
    
    #sets a loop to check the user name matches
    while checked_login != username: 
        failed_input = input("type 'try again' or type 'exit' to quit: \n")
        
        if failed_input.lower() == "try again":
            checked_login = input("Enter username: \n")
        
        elif failed_input.lower() == "exit":
            print("Exiting login process.")
            return False  # Return False to indicate the login failed
        
        else:
            print("Invalid option.")
    
    checked_password = input("Enter password: \nyou have 3 attempts \n ")
    password_attempts = 3

    while checked_password != password and password_attempts > 0: #sets a loop to check the user name matches
        password_attempts = password_attempts - 1
        print("you have " + str(password_attempts) + " left ")
        checked_password = input("Enter password: \n")


        if password_attempts == 1:
            print("get out you dam hacker")
            exit()     
                            
        #failed_input = input("wrong password type 'try again' or type 'exit' to quit: ")
        
        #if failed_input.lower() == "try again":
            #checked_password = input("Enter password: ")
            #continue
       
        #elif failed_input.lower() == "exit":
            #print("Exiting login process.")
            #return False  # Return False to indicate the login failed
        
        #else:
            #print("Invalid option.")

    print(checked_login + " logged in")
    print(type(checked_login))
    return True # Return True to indicate a successful login

while True:
    reg_status = input('enter the following "login" or "sign up" or "exit" \n') 
    
    if reg_status == "sign up":
        new_username = input("enter new username: \n" ) 
        enter_username(new_username)
        new_password = input("enter new password. Must contain, lower case, upper case, special character, number. must be between 8 - 15 characters: \n")
        enter_password(new_password)
        continue
    
    #this it the login step
    elif reg_status == "login":
        checked_login = input("enter username: ")
        
        if check_login(checked_login): #same as if check_username(checked_username) == True:
           break

    #added exit
    elif reg_status == "exit":
        break
    
    else:
        print("Invalid option. Try again. \n")