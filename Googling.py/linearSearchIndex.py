# Linear Index
# Print index if found

names = ["Debbie", "Jessie", "Vigdis", "Emilia"]
searchValue = "Vigdis"
found = False
index = 0


while not found and index < len(names):
    if searchValue == names[index]:
        found = True
    else:
        index += 1


if found:
    print("Found at position:", index)
else:
    print("Not found! :<")