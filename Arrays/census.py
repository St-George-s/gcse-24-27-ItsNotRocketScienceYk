#Task 1 - Create an Array
# cityNames = ["London", "Edinburgh", "Cardiff", "Belfast", "Glasgow"]
# for counter in range (len(cityNames)):
#     print (cityNames[counter])

#Task 2 - Parallel Arrays + Print using a Loop
# cityNames = ["London", "Edinburgh", "Cardiff", "Belfast", "Glasgow"]
# population = [8908, 482, 366, 341, 635]
# for counter in range (len(cityNames)):
#     print (cityNames[counter] + " has a population of " + str(population[counter]))

#Task 4 - Linear Search for population
found = False
userCity = input("What city would you like population for?: ")
cityNames = ["london", "edinburgh", "cardiff", "belfast", "glasgow"]
population = [8908, 482, 366, 341, 635]

for counter in range (len(cityNames)):
    if userCity == cityNames[counter]:
        print (cityNames[counter] + " has a population of " + str(population[counter]))
        found = True
if not found:
    print("Your city was not found :/")
