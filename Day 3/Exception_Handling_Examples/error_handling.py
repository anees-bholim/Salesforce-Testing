try:
    username = input("Enter username: ")
    if username == "":
        raise Exception("Username cannot be empty")
    print("Login Started")
    
except Exception as e:
    print("Error: ", e)