 #Find the area of a rectangle (Function)

#Length and Breadth are parameters
def getAreaRectangle(length, breadth):
   return length * breadth

#Call a subprograms
print("START")

print(getAreaRectangle(123, 456))

returnedArea = getAreaRectangle(43, 89)
print(returnedArea)

secondReturnedArea = getAreaRectangle(5, 4)

if returnedArea > secondReturnedArea:
   print("First area is bigger")