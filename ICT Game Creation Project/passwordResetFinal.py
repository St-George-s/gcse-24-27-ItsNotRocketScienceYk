password = ""
username = ""
lowercase = 0
uppercase = 0

valid = False
while not valid:
    password = input("Enter new password: ")
    
    lowercase = 0
    uppercase = 0
    
    for char in password:
        if ord(str(char)) >= 65 and ord(str(char)) <= 90:
            uppercase = uppercase + 1
        if ord(str(char)) >= 97 and ord(str(char)) <= 122:
           lowercase = lowercase + 1
    
    if len(password) >= 8 and lowercase > 0 and uppercase > 0:
        print("Password is valid.")
        valid = True
        Newpassword = input("Re-enter new password to confirm: ")
        if Newpassword == password:
            print("Password confirmed.")
            print("Password has been reset :)")
        else:
            print("Passwords do not match.")
            valid = False
    else:
        if len(password) < 8:
            print("Password is not long enough.")
        if lowercase == 0:
            print("Password does not contain lowercase letters.")
        if uppercase == 0:
            print("Password does not contain UPPERCASE letters.")

specialCharFound = False 
for char in password:
    asciiVal= ord(char)
    if (asciiVal >= 33 and asciiVal <= 47) or (asciiVal >= 58 and asciiVal <= 64) or (asciiVal >= 91 and asciiVal <= 96) and (asciiVal>= 123 and asciiVal <= 126):
        specialCharFound = True

while valid != False:
    if specialCharFound and len(password) > 12:
        print("Password is strong :)")
    elif specialCharFound or len(password) > 9:
        print("Password is moderate :|")
    else:
        print("Password is weak :(")