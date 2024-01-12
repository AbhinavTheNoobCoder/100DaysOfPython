#DAY 34 - Dictionary methods
contacts = {}
while True:
    action = input('''What change would you like to make in Contacts?
Press -
A for Adding a contact
D for Deleting a contact
C for Clearing all contacts
U for Updating a contact
                   
Press Q to Quit
>>> ''').lower()
    if action == "a":
        addition = input("Enter contact name: ")
        email = input("Enter their email address: ")
        phone = int(input("Enter their phone number: "))
        contacts[addition] = [email, phone] #contacts.update({addition: [email, phone]}) works
    elif action == "d":
        deletion = input("Enter contact to be deleted: ")
        contacts.pop(deletion, "Contact not found in dictionary")
    elif action == "c":
        contacts.clear()
    elif action == "u":
        updated = input("Enter contact to be updated: ")
        if updated in contacts:
            opt1 = input("Update email? (y/n): ").lower()
            if opt1 == 'y':
                email = input("Enter updated email address: ")
                contacts[updated][0] = email
            opt2 = input("Update phone number? (y/n): ").lower()
            if opt2 == 'y':
                phone = int(input("Enter updated phone number: "))
                contacts[updated][1] = phone
        else:
            print("Contact not found.")
    elif action == 'q':
        break
    else:
        print("Action not recognised.")
print("Contacts -", contacts)