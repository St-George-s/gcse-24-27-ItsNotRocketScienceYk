import random

number = str(random.randint(1000, 9999))
#print(number)  # remove this before submitting

tries = 0
guess = input("Enter a 4-digit guess: ")

while guess != number:

    if guess.isdigit() and len(guess) == 4:

        tries = tries + 1
        match_count = 0
        alreadyGuessed = []

        for char in guess:
            if char in number and char not in alreadyGuessed:
                match_count = match_count + 1
                alreadyGuessed.append(char)
                print("Found a match!",char," is correct :)")

    else:
        print("4 NUMBERS ONLY >:(")
        guess = input("Try again, 4-digits only!: ")

    guess = input("Enter a 4-digit guess: ")

tries = tries + 1
print("Well done! You guessed the correct number :3")
print("It took you", tries, "tries.")