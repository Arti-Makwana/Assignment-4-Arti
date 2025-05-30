#Ask the user for a number and print its square (the product of the number times itself).

#Here's a sample run of the program (user input is in bold italics):

#Type a number to see its square: 4

#4.0 squared is 16.0
def main():
    # Ask the user for a number
    number = float(input("Type a number to see its square: "))

    # Calculate the square
    square = number * number

    # Print the result
    print(f"{number} squared is {square}")

# Run the program
if __name__ == "__main__":
    main()
