import hashlib

stored_username = "remsha imtiaz"
stored_password = hashlib.sha256("0123".encode()).hexdigest()

Username = input("Enter Your username: ").lower()
Password = input("Enter Your password: ")

hashed_password = hashlib.sha256(Password.encode()).hexdigest()

if Username == stored_username and hashed_password == stored_password:
    print("Login Successful")
else:
    print("Invalid Login")
