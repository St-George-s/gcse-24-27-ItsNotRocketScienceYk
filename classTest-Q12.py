# Question 12 - Santa's elves
import random 

for counter in range(1,11): 

    randScore = random.randint(1,100) 

    if randScore > 50: 

        print("Child:",counter, "Your score is", randScore, "Good! You will recieve a gift :)") 

    elif randScore <= 50: 

        print("Child:",counter, "Your score is", randScore, "Naughty! You will not recieve a gift :(") 
