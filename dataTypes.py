#data types:P
name = "Devansshi" #This is a string
myAge = 14 #This is an integer
height = 0.0000000000000000001 #This is a float (Decimal Number/Real)
isAnnoying = True #This is a boolean (True/False)

#Casting (Changing from one Data type to another)
age = input("Enter age: ")
print (age)
print (age + "10") #concatenate two string together (join them)
ageAsAnInt = int(age)
print (ageAsAnInt + 10) #Add 2 integers together (maths)
print ("Ur age is " + str(ageAsAnInt))

#Data Types - more examples
stillAnInteger = -4
myNumber = "087634254398" #Always store as a string

#Arithmatic operators
add = 10 + 10
subtract = 10 - 10
multiply = 10 * 10
division = 10 / 10 #Will output a float
integerDivision = 11 // 10 #Integer forces output to be a whole number (rounds)
print(add, subtract, multiply, division) 
print(integerDivision)
modulo = 2000 % 501 #Remainder of the division
print(modulo)
exponent = 2 ** 3 # To the power of
print(exponent)

#Activity 1 - Take two inputs, multiply them together and output answer

age = input("Enter age: ")
brainCapcityasInt = int("brainCapacity")
brainCapacity = input("Enter brain capacity: ")
print (age * brainCapacityasInt)


#Activity 2 - Input user's age, output age times 7

#Activity 3 - Take radius as input, output volume of a sphere (V = 4/3 x pi x r^3)