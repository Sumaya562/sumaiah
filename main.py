import re

contact = {}


def display_contact():
    print("Name\t\tContact Number\t\tEmail")
    for key in contact:
        contact_info = contact[key]
        print(f"{key}\t\t{contact_info['phone']}\t\t{contact_info['email']}")


def is_valid_name(name):
    """Validates the contact name."""
    if not re.match(r"^[A-Za-z\s]+$", name):
        print("Only letters and spaces are allowed in the name.")
        return False
    return True


while True:
    try:
        choice = int(input(
            "1. Add New Contact\n2. Search Contact\n3. Display Contacts\n4. Update Contact\n5. Delete Contact\n6. Exit\nEnter your choice: "))
        if choice == 1:
            name = input("Enter the contact name: ")
            if not is_valid_name(name):  #Check if name is valid before adding
                continue  # Skip adding the contact if name is invalid
            phone = input("Enter the mobile number: ")
            address = input("Enter your address or district: ")
            email = input("Enter your Email: ")
            contact[name] = {"phone": phone, "address": address, "email": email}
            print("Contact added successfully!\n")

        elif choice == 2:
            search_name = input("Enter the contact name to search: ")
            if search_name in contact:
                contact_info = contact[search_name]
                print(
                    f"{search_name}'s contact number is {contact_info['phone']}, Address: {contact_info['address']}, Email: {contact_info['email']}")
            else:
                print("Name not found in the contact book.\n")

        elif choice == 3:
            if not contact:
                print("Contact book is empty.\n")
            else:
                display_contact()

        elif choice == 4:
            update_contact = input("Enter the contact you need to update: ")
            if update_contact in contact:
                phone = input("Enter your new mobile number: ")
                address = input("Enter your new address or district: ")
                email = input("Enter your new Email: ")
                contact[update_contact] = {"phone": phone, "address": address, "email": email}
                print("Contact updated successfully!")
                display_contact()
            else:
                print("Name not found in the contact book.\n")

        elif choice == 5:
            del_contact = input("Enter the contact name to be deleted: ")
            if del_contact in contact:
                confirm = input(f"Do you want to delete {del_contact}'s contact? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    del contact[del_contact]
                    print("Contact deleted successfully!")
                    display_contact()
                else:
                    print("The deletion was canceled.\n")
            else:
                print("The name is not found in the contact book.\n")

        elif choice == 6:
            print("EXITING THE PROGRAM. GOODBYE!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")