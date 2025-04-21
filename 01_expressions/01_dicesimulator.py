import random

def roll_dice():
    # Local scope: die1 and die2 exist only inside this function
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"Die 1: {die1}, Die 2: {die2}")

def main():
    # Rolling dice 3 times
    print("Rolling dice 3 times...\n")
    for i in range(1, 4):
        print(f"Roll {i}:")
        roll_dice()
        print()

# Run the main function
if __name__ == "__main__":
    main()
