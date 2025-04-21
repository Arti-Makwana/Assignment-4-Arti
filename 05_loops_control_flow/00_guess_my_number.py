#Guess My Number

#I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

#Enter a new number: 25 Your guess is too low

#Enter a new number: 40 Your guess is too low

#Enter a new number: 45 Your guess is too low

#Enter a new number: 48 Congrats! The number was: 48


import random

def main():
    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    guess = None
    while guess != secret_number:
        try:
            guess = int(input("Enter a guess: "))
            if guess > secret_number:
                print("Your guess is too high\n")
            elif guess < secret_number:
                print("Your guess is too low\n")
            else:
                print(f"Congrats! The number was: {secret_number}")
        except ValueError:
            print("Please enter a valid number.\n")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
