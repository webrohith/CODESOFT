import json
from inputimeout import inputimeout, TimeoutOccurred

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=2)

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}")
            print("-" * 20)

def add_contact():
    print("\nAdding a new contact:")
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")

    contacts = load_contacts()
    new_contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!")

def search_contact(query):
    contacts = load_contacts()
    results = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            results.append(contact)
    return results

def update_contact(name):
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"\nUpdating contact '{name}':")
            contact['phone'] = input("Enter the new phone number: ")
            contact['email'] = input("Enter the new email: ")
            contact['address'] = input("Enter the new address: ")
            save_contacts(contacts)
            print(f"Contact '{name}' updated successfully!")
            return
    print(f"Contact '{name}' not found.")

def delete_contact(name):
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"\nContact '{name}' deleted successfully!")
            return
    print(f"Contact '{name}' not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Display Contacts\n2. Add Contact\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")

        try:
            choice = inputimeout(prompt="Enter your choice (1-6): ", timeout=10)
        except TimeoutOccurred:
            print("\nTimeout. Exiting the Contact Book. Goodbye!")
            break

        if choice == '1':
            contacts = load_contacts()
            display_contacts(contacts)
        elif choice == '2':
            add_contact()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = search_contact(query)
            display_contacts(results)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            update_contact(name)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    print("Welcome to the Contact Book!")
    main()
