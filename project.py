count = 0
password = ""
lowercase = 0
uppercase = 0

password = input("Enter your password: ")
while len(password) < 8:
    print("Password is not long enough.")
    password = input("Enter your password again: ")
print("Password is valid")

while ord(str(password)) >= 65 and ord(str(password)) <= 90:
    print("Password includes UPPERCASE :)")
print("Password is invalid, try again.")

while ord(chr) >= 97 and ord(chr) <= 122:
    print("Password includes lowercase")
print("Password is invalid, try again.")