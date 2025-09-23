swimTime = float(input("Enter swim time: "))
if swimTime < 60.0:
    print("Participant qualifies")
else:
    print("Participant does not qualify")

swimTime = float(input("Enter swim time: "))
if swimTime < 55.0:
    print("Participant qualifies for GOLD category")
elif swimTime > 55.0 and swimTime < 60.0:
    print("Participant qualifies for SILVER category")
elif swimTime > 60.0 and swimTime < 65.0:
    print("Participant qualifies for SILVER category")
else:
    print("Participant does not qualify")