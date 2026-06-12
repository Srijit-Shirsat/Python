username = input("Enter your username: ")
password = input("Enter your password: ")

if username=="":
    print("username cannot be empty")
elif username.strip() == "":
    print ("username cannot contain only spaces")
elif len(username)<4:
    print ("username should be more than 4 characters") 
    
elif password=="":
    print ("password cannot be empty")
elif len(password)<8:
    print ("password must be more than 8 characters")
elif password.lower() == "password" or password == "12345678":
    print ("password is too weak. Please enter a strong password")
    
else :
    print ("Login credentials accepted")