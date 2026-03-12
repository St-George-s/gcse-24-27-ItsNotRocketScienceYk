# Linear Search
# Create an array

names = ["Debbie", "Jessie", "Vigdis", "Emilia"]
searchValue = "Jessie"
found = False
index = 0

#Conditional Loop - Stops when 
# 1. Search value is found
# 2. Search value is at the end of the array "names"
while not found and index < len(names):
    if searchValue == names[index]:
        found = True
    else:
        index += 1

#After the loop (unindent)

if found:
    print("Found! :>")
else:
    print("Not found! :<")
#<><><><><><><><><><><><><><><><><><><><><><><><><><><>