#MAX_LENGTH = 3

MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print("Removed:", removed)


def main():
    num_items = int(input("How many items in your list? "))
    user_list = []

    for i in range(num_items):
        item = input(f"Enter item {i + 1}: ")
        user_list.append(item)

    shorten(user_list)
    print("Final list:", user_list)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

