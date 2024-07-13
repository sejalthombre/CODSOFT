contacts = {}

while True:
    choice = int(input("\nEnter choice:\n1. Add Contacts\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\n"))

    match choice:
        case 1:
            n = input("Enter Name: ")
            m = input("Enter Mobile Number: ")
            e = input("Enter Email: ")
            a = input("Enter Address: ")
            contacts[m] = (n, e, a)
            print("Contact Added!")

        case 2:
            if not contacts:
                print("No contacts found.")
            else:
                for k, v in contacts.items():
                    print(f"Mobile Number: {k}")
                    print(f"Name: {v[0]}")
                    print(f"Email: {v[1]}")
                    print(f"Address: {v[2]}\n")

        case 3:
            search_term = input("Enter name or phone number to search: ")
            found = False
            for mobile, details in contacts.items():
                if search_term.lower() in details[0].lower() or search_term == mobile:
                    print(f"Name: {details[0]}")
                    print(f"Mobile Number: {mobile}")
                    print(f"Email: {details[1]}")
                    print(f"Address: {details[2]}\n")
                    found = True
            if not found:
                print("No contacts found.")
                
        case 4:
            update_contact = input("Enter the Mobile Number to update: ")
            if update_contact in contacts:
                n = input(f"Enter new Name (current: {contacts[update_contact][0]}): ")
                e = input(f"Enter new Email (current: {contacts[update_contact][1]}): ")
                a = input(f"Enter new Address (current: {contacts[update_contact][2]}): ")
                new_m = input(f"Enter new Mobile Number (current: {update_contact}): ")

                if new_m != update_contact:
                    contacts[new_m] = (n, e, a)
                    del contacts[update_contact]
                else:
                    contacts[update_contact] = (n, e, a)
                
                print("Contact updated successfully!")
            else:
                print("Contact not found.")
                
        case 5:
            delete_contact = input("Enter the Mobile Number to delete: ")
            if delete_contact in contacts:
                del contacts[delete_contact]
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")


        case _:
            print("Invalid choice. Please enter a valid choice.")
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            update_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Thank you for using the Contact Management System!")

