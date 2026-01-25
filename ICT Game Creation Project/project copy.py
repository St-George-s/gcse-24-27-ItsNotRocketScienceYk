password = ""
username = ""
lowercase = 0
uppercase = 0


password = input("Enter new password: ")

while len(password) < 8:
    print("Password is not long enough.")
    password = input("Enter password again: ")

lowercase = 0
uppercase = 0
for count in password:
    if count.islower():
        lowercase = lowercase + 1
    if count.isupper():
        uppercase = uppercase + 1
    
while lowercase == 0:
    print("Password does not contain lowercase letters")
    password = input("Re-enter password: ")
    lowercase = 0
    uppercase = 0
    for count in password:
        if count.islower():
            lowercase = lowercase + 1
        if count.isupper():
            uppercase = uppercase + 1


while uppercase == 0:
    print("Password does not contain UPPERCASE letters")
    password = input("Re-enter password: ")
    lowercase = 0
    uppercase = 0
    for count in password:
        if count.islower():
            lowercase = lowercase + 1
        if count.isupper():
            uppercase = uppercase + 1

print("Password has been reset :)")
    
    