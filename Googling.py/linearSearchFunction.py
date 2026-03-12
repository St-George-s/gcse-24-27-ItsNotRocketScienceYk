# Linear Function

def linearSearch (searchValue, searchList):

    found = False
    index = 0


    while not found and index < len(searchList):
        if searchValue == searchList[index]:
            found = True
        else:
            index += 1


    if found:
        print("Found! :>")
    else:
        print("Not found! :<")

#Call out
linearSearch("Devansshi", ["Liyana", "Maggie", "Alina", "Devansshi"])
linearSearch("Alina", ["Debbie", "Jessie", "Vigdis", "Emilia"])
linearSearch("Supercalifragilisticexpialidocious", ["Debbie", "Jessie", "Vigdis", "Emilia"])
