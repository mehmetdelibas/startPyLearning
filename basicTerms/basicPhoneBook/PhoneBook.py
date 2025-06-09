from PhoneClass import PhoneBook


pb=PhoneBook()

while True:
    print("\n----Phone Book----")
    print("1 - Add Contact")
    print("2 - List Contact")
    print("3 - Deleted Contact")
    print("4 - Exit")

    choice = int(input("Make your choice"))

    if choice==1:
        firstName = input("First Name =")
        lastName = input("Last Name =")
        phoneNumber = input("Phone Number =")
        pb.addContact(firstName,lastName,phoneNumber)

    if choice==2:
        pb.listContacts()
        continue
    if choice==3:
        name = input("Enter the name of the contact you want to delete = ")
        pb.deleteContact(name)
    if choice==4:
        print("Exiting...")
    elif choice>4 or choice<1: 
        print("Invalid choice, please try again!")