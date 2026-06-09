#procedure
def printName(name):
    print(name)

#function with one parameter name
def printNameFunc(name):
    return name

#Call the procedure
printName("Liyana")

#Call the function and print returned value
print(printNameFunc("Jessie"))

#Call the function and store returned value in a variable
returnedName = printNameFunc("Alina")
print(returnedName)