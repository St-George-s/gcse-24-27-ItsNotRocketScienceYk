# Question 12 - exploring "random"
import random 

for counter in range(1,11): 

   # randScore = random.randint(1,100) 

    if random.randint(1,100)  > 50: 

        print("Child:",counter, "Your score is", random.randint(1,100) , "Good! You will recieve a gift :)") 

    elif random.randint(1,100) <= 50: 

        print("Child:",counter, "Your score is", random.randint(1,100) , "Naughty! You will not recieve a gift :(") 
