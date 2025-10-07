# heightone = 2.4
# heighttwo = 3.8
# heightthree = 0.4
#Create arrays
heights = [2.4, 3.8, 0.4, 1.9]
names = ["Bippity", "Boppity", "Bob"]
print(names[2], heights[2]) #prints Bob, prints 2.4

#Loop over names array and print
for counter in range(len(names)):
    print(names[counter]) #counter is 0 then 1 then 2
    print(heights[counter])

# Append (Add) to an array
heights.append(2.2)
names.append("Blob")

print(heights)
print(names)