def main():
    # Ask the user to enter a measurement in feet
    feet = float(input("Enter measurement in feet: "))

    # Convert feet to inches (12 inches in 1 foot)
    inches = feet * 12

    # Print the result
    print(f"{feet} feet is {inches} inches.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
