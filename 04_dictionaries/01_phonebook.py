def main():
    phonebook = {}

    while True:
        name = input("Enter a name: ")

        if name.strip() == "":
            break

        phone = input("Enter a phone number for " + name + ": ")
        phonebook[name] = phone

    print("\nPhonebook entries:")
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
