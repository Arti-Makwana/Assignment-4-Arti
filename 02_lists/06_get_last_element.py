def get_last_element(lst):
    print("The last element is:", lst[-1])


def main():
    num_elements = int(input("How many elements are in the list? "))
    user_list = []

    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    get_last_element(user_list)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
