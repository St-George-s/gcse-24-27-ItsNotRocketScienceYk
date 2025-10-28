with open("/workspaces/gcse-24-27-ItsNotRocketScienceYk/File handling/holiday.txt", "r") as file:
    counter = 0
    for liyana in file:
        counter = counter + 1 #OR counter += 1
    print("There are", counter, "lines")