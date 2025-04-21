#This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

#An example run of the program looks like this (user input is in blue):

#Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


def main():
    number_counts = {}

    while True:
        user_input = input("Enter a number: ")

        if user_input.strip() == "":
            break

        try:
            num = int(user_input)
            if num in number_counts:
                number_counts[num] += 1
            else:
                number_counts[num] = 1
        except ValueError:
            print("Please enter a valid integer.")

    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
