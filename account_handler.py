class account_handler:
    username = None
    password = None

    def __init__(self):
        print("username")
    
    def password(self):
        print("password")
    
    #method that asigns new username    
    def enter_username(self):
        self.username = input("enter new username: \n" )
        print(self.username + " is now your username, welcome \n")
        
    #method that asigns new password and verfiy
    def enter_password(self):
        self.password = input("enter new password. Must contain, lower case, upper case, special character, number: \n")
        
        lower_case = False
        upper_case = False
        num = False
        special = False

        for char in self.password:
            
            if char.islower():
                num = True
            if char.isupper():
                lower_case = True
            if char.isdigit():
                upper_case = True
            if  not char.isalnum():
                special = True
        if lower_case and upper_case and num and special:
            print("vaild password ")
            return True
                
        else:
            print("bad ")
            return False
    
    #check login
    def check_username(self):
        username = input("Enter username: \n")
        if username != self.username:
            print("User name " + username + " does not match records")
            return False
        else:
            return True
        
    #check passward login
    def check_password(self):
        password_attempts = 3
        password = None
        while password != self.password:
            password = input(str(password_attempts) + " attemts at password \nEnter password: \n")
            if password_attempts == 0:
                print("get out you dam hacker")
                exit()
            password_attempts -= 1
        return True
          
        

        
            
        
        
        
    