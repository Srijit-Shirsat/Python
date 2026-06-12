username = input("Enter username: ")

if username == "":
    print("username cannot be empty")
elif username.strip() == "":
    print ("username cannot have only spaces")
elif len(username) < 4:
    print ("username should contain more than 4 characters")
elif " " in username:
    print ("Spaces are not allowed in username")
elif "@" in username or "#" in username:
    print ("username contains forbidden characters")
    
else:
    print ("Username is valid")
    
 