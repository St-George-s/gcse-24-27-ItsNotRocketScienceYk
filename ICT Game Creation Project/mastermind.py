import random
number = random.randint(1000, 9999)
guess = input("Enter a 4-digit guess: ")

while guess != number:
    if len(guess) != 4:
        print("4 NUMBERS ONLY YOU PRICK")
        guess = input("Try again, 4-digits only!: ")
    elif len(guess) == 4:
        for count in range(1, 4):
            print("guess is wrong, try again!")
            guess = input("Enter a 4-digit guess: ")
    print (number, "is right answer!")
print("Well done! You guessed the correct number :3")
    

#print"The random number is:", number