
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
# x = int(input("Enter number: "))
# list = [1, 2, 3, 4, 5]

# Match = False

# for i in range(0, len(list)):
#     print(list[i])
#     if x == list[i]:
#         Match = True

# if Match == True:
#     print("Number found!")
# else:
#     print("Number not found...")


# x = ["S", "T", "R", "I", "N", "G"]
# y = ["S, t, r, i, n, g"]
# z = "sTrInG"

# print(z[-2:])

##String Manipulation
# surname = input("State your surname")
# age = str(input("State your age (2 digits): "))
# town = input("Town: ")

# #first 3 letters of town in uppercase + age as 2 digits + first and last letter of your surname
# username = town[0:3].upper() + age + surname[0].lower() + surname[len(surname) - 1].lower()

# print(username)

# word = input("Input a word: ")

# firstLetter = word[0]
# #first character removed and the last character replaced with the original first character
# newWord = word[1:len(word)-1] + firstLetter

# print(newWord)

# b = int(input("Enter a number: "))
# x = 1
# while x <= 100:
#     print(b*x)
#     x = x + 1

# age = int(input("Enter your age: "))

# for i in range(age):
#     print("happy birthday)

x = int("123")
y=x*10
print(x)