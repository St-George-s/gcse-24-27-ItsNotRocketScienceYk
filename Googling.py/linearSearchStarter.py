authorised = [True, True, False]
searchValue = False
found = False
index = 0

while not found and index < len(authorised):
    if searchValue == authorised[index]:
        found = True
    else:
        index += 1

if found:
    print("Found! :>")
else:
    print("Not found! :<")