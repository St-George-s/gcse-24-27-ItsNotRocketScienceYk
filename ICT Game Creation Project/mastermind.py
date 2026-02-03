import random
number = str(random.randint(1000, 9999))
print(number)
guess = input("Enter a 4-digit guess: ")

while guess != number:
    if len(guess) != 4:
        print("4 NUMBERS ONLY YOU PRICK")
        guess = input("Try again, 4-digits only!: ")
    elif len(guess) == 4:
        alreadyGuessed = []
        for char in guess:
            for charTwo in number:
                if char == charTwo:
                    if char not in alreadyGuessed:
                        alreadyGuessed.append(char)
                        
                        print("Found a match")
                        print(char, " is in the word")
    guess = input("Enter a 4-digit guess: ")
  
   

print("Well done! You guessed the correct number :3")
    

#print"The random number is:", number