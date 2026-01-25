password = ""
username = ""
lowercase = 0
uppercase = 0

valid = False
while not valid:
    password = input("Enter new password: ")
    
    lowercase = 0
    uppercase = 0
    
    for count in password:
        if count.islower():
            lowercase += 1
        if count.isupper():
            uppercase += 1
    
    if len(password) >= 8 and lowercase > 0 and uppercase > 0:
        print("Password has been reset :)")
        valid = True
    else:
        if len(password) < 8:
            print("Password is not long enough.")
        if lowercase == 0:
            print("Password does not contain lowercase letters.")
        if uppercase == 0:
            print("Password does not contain UPPERCASE letters.")