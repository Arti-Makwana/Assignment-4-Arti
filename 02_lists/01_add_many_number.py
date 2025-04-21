def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    # Example list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Call the sum function and print the result
    result = sum_numbers(numbers)
    print(f"The sum of {numbers} is {result}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
