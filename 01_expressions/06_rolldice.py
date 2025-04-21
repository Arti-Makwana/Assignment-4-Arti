import random

def main():
    # Roll the first die
    die1 = random.randint(1, 6)
    
    # Roll the second die
    die2 = random.randint(1, 6)
    
    # Calculate the total
    total = die1 + die2

    # Print the results
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

# Call the main function
if __name__ == '__main__':
    main()
