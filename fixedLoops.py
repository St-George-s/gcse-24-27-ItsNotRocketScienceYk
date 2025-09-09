# #Example
# for counter in range(10):
#     print(counter)

# #Question 1
# for counter in range(10):
#     print("Devansshi")

# #Question 2 - Ask my name
# name = input("Enter name: ")
# #print it 1000 times
# for counter in range (1000):
#     print(name)

# #Question 3 - ask for name
# name = input("ENTER NAME NOW: ")
# #print hello then name 1000 times
# for counter in range(1000):
#     print ("Hello " + name)

# #Question 4 - answers to 8 times table (1-12)
# for counter in range(1, 13):
#     print(counter * 8)

# #Question 5 - answers to the 8 times table from 1 to 1000. 
# for counter in range(1, 1001):
#     print(counter * 8)

# #Question 6 - Calculate the 7 times table up to 12. 
# for counter in range(1, 13):
# #Print "7 x number = answer" each time. 
#     print(counter, "x 7", "=", counter * 7)

# #Question 7 - ask the user to input the age of 10 people and print each age. 
# for counter in range (10):
#     age = input("ENTER YOU AGE: ")
#     print(age)

# #Question 8 - Ask the user to input the age of 10 people. 
# for counter in range (10):
#     age = input("ENTER AGE NOW")
#     newAge = int(age) + 10
#     print(newAge)

# Question 9 - Ask the user to input the age of 10 people. 
# total = 0
# for counter in range (10):
#     age = int(input("Enter age pls: "))
# #Add up all the ages
#     total = total + age
# #Print the total ages
#     print(total)

#Question 10 - Write a Python program to output the 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12 times tables from 1 to 12. 
for counter1 in range(1,13):
    print ("")
    print (counter1, " Times table")
    for counter2 in range(1,13):
        print(counter1, "x", counter2, " = ", counter1 * counter2)
