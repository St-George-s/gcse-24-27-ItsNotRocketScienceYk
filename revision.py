password = 0
username = ""

## IF STATEMENTS --- SELECTION STATEMENT
# x = input("Enter passcode: ")

# if x == "GO":
#     print("Access granted")
# else:
#     print("Access denied")

# x = input("Enter passcode: ")
# usertype = input("Enter usertype: ")

# if x == "GO":
#     if usertype == "teacher":
#         print("Unrestricted access granted")
#     else:
#         print("Restricted access granted")
# else:
#     print("Access denied")

## - Arrays
x = int(input("Enter number: "))
list = [1, 2, 3, 4, 5]

Match = False

for i in range(0, len(list)):
    print(list[i])
    if x == list[i]:
        Match = True

if Match == True:
    print("Number found!")
else:
    print("Number not found...")