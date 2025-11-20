totalHeight = 0
counter = 0

for i in range(12):
    height = int(input("State your height: "))
    totalHeight = totalHeight + height
    counter = counter + 1
print("Average is ", totalHeight/counter) 