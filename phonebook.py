import csv
from os import system

class Contact:

    def __init__(self, firstName, lastName, phone, email):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.email = email


    def __str__(self):
        return f"{self.firstName} {self.lastName}: {self.phone} ; {self.email}"


class Phonebook:

    def __init__(self):
        self.contacts = []
        self.copy = []
        self.dirty = False


    def backup(self):
        self.copy = self.contacts


    def add_contact(self, contact):
        self.backup()
        self.contacts.append(contact)
        self.dirty = True
    

    def delete_contact_by_firstName(self, firstName):

        self.backup()
        quest = input("Are you sure you want to delete the contact? Y/N").lower()
        if quest == "y":
            newAgenda = []
            for contact in self.contacts:
                if contact.firstName != firstName:
                    newAgenda.append(contact)
        
            self.contacts = newAgenda
            self.dirty = True


    def delete_contact_by_lastName(self, lastName):

        self.backup()
        quest = input("Are you sure you want to delete the contact? Y/N").lower()
        if quest == "y":
            newAgenda = []

            for contact in self.contacts:
                if contact.lastName != lastName:
                    newAgenda.append(contact)
        
            self.contacts = newAgenda
            self.dirty = True


    def delete_contact_by_phone(self, phone):

        self.backup()
        quest = input("Are you sure you want to delete the contact? Y/N").lower()
        if quest == "y":
            newAgenda = []
            for contact in self.contacts:
                if contact.phone != phone:
                    newAgenda.append(contact)
        
            self.contacts = newAgenda
            self.dirty = True
    

    def edit_contact(self, old_firstName, old_lastName, new_firstName, new_lastName, new_phone, new_email):

        self.backup()
        quest = input("Are you sure you want to edit the contact? Y/N").lower()
        if quest == "y":
            for contact in self.contacts:

                if contact.firstName == old_firstName and contact.lastName == old_lastName:
                    contact.firstName = new_firstName
                    contact.lastName = new_lastName
                    contact.phone = new_phone
                    contact.email = new_email
                    return True
            
            return False
        self.dirty = True
    

    def search_contact(self, firstName, lastName):

        for contact in self.contacts:
            if contact.firstName == firstName and contact.lastName == lastName:
                return contact
        return None


    def search_contact_by_firstName(self, firstName):
        
        for contact in self.contacts:
            if contact.firstName == firstName:
                return contact
            
        return None
    

    def search_contact_by_lastName(self, lastName):
        
        for contact in self.contacts:
            if contact.lastName == lastName:
                return contact
                
        return None


    def search_contact_by_phone(self, phone):
        
        for contact in self.contacts:
            if contact.phone == phone:
                return contact
            
        return None


    def search_contact_by_email(self, email):
        
        for contact in self.contacts:
            if contact.email == email:
                return contact
            
        return None


    def display_contacts(self):
        for copy_contact in self.copy:
            print(copy_contact)
        for contact in self.contacts:
            print(contact)
        

    def sort_contacts_by_firstName(self, type):

        self.backup()
        n = len(self.contacts)

        if type == "ascending":
            for i in range(n):
                for j in range(n-i-1):

                    if self.contacts[j].firstName > self.contacts[j+1].firstName:
                        aux = self.contacts[j]
                        self.contacts[j] = self.contacts[j+1]
                        self.contacts[j+1] = aux

        elif type == "descending":
            for i in range(n):
                for j in range(n-i-1):

                    if self.contacts[j].firstName < self.contacts[j+1].firstName:
                        aux = self.contacts[j]
                        self.contacts[j] = self.contacts[j+1]
                        self.contacts[j+1] = aux
    
        self.dirty = True


    def sort_contacts_by_lastName(self, type):

        self.backup()
        n = len(self.contacts)

        if type == "ascending":
            for i in range(n):
                for j in range(n-i-1):

                    if self.contacts[j].lastName > self.contacts[j+1].lastName:
                        aux = self.contacts[j]
                        self.contacts[j] = self.contacts[j+1]
                        self.contacts[j+1] = aux

        elif type == "descending":
            for i in range(n):
                for j in range(n-i-1):

                    if self.contacts[j].lastName < self.contacts[j+1].lastName:
                        aux = self.contacts[j]
                        self.contacts[j] = self.contacts[j+1]
                        self.contacts[j+1] = aux

        self.dirty = True


    def undo_operation(self):
        if self.copy:
            self.contacts = self.copy.pop()
            print("Operation undo.")
        else:
            print("Operation undo failed.")


    def save_contacts_to_file(self, filename):

        with open(filename, mode = "w", newline ="") as file:
            writer = csv.writer(file)
            writer.writerow(["Firstname", "Lastname", "Phone", "Email"])
            for contact in self.contacts:
                writer.writerow([contact.firstName, contact.lastName, contact.phone, contact.email])
    

    def load_contacts_from_file(self, filename):

        try:

            with open(filename, mode = "r") as file:
                reader = csv.reader(file)
                next(reader)
                self.contacts = []
                for row in reader:
                    if row:
                        self.contacts.append(Contact(*row))

        except FileNotFoundError:
            print(f"File {filename} not found.")


class Menu:

    def __init__(self):
        self.phonebook = Phonebook()
    

    def display_menu(self):
        print("\nPhonebook Menu")
        print("01. Display Contacts")
        print("02. Add Contact")
        print("03. Delete Contact")
        print("04. Edit Contact")
        print("05. Search Contact")
        print("06. Sort Contacts")
        print("07. Save Contacts", end = "")
        if self.phonebook.dirty == True:
            print("*")
        else:
            print(" ")
        print("08. Load Contacts")
        print("09. Undo")
        print("10. Exit")
    

    def add_contact(self):
        
        firstName = input("Enter first name: ").capitalize()
        lastName = input("Enter last name: ").capitalize()
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contact = Contact(firstName, lastName, phone, email)
        self.phonebook.add_contact(contact)
        print(f"Contact {firstName} {lastName} added.")

    
    def delete_contact(self):

        type = input("What do you want to remove? Firstname, lastname or phone: ").lower()

        if type == "firstname":
            firstName = input("Enter the first name of the contact to delete: ")
            self.phonebook.delete_contact_by_firstName(firstName)            
            print(f"Contact(s) with first name {firstName} deleted.")

        elif type == "lastname":
            lastName = input("Enter the last name of the contact to delete: ")
            self.phonebook.delete_contact_by_lastName(lastName)
            print(f"Contact(s) with last name {lastName} deleted.")
        
        elif type == "phone":
            phone = input("Insert the phone number of the contact to delete: ")
            self.phonebook.delete_contact_by_phone(phone)
            print(f"Contact with phone number {phone} deleted.")
        
        else:
            print(f"Option {type} not available. Please try again.")

    
    def edit_contact(self):
        
        old_firstName = input("Enter the first name of the contact to edit: ")
        old_lastName = input("Enter the last name of the contact to edit: ")
        contact = self.phonebook.search_contact(old_firstName, old_lastName)

        if contact:
            new_firstName = input(f"Enter the new first name (current: {contact.firstName}): ")
            new_lastName = input(f"Enter the new last name (current: {contact.lastName}): ")
            new_phone = input(f"Enter the new phone number (current: {contact.phone}): ")
            new_email = input(f"Enter the new email (current: {contact.email}): ")
            self.phonebook.edit_contact(old_firstName, old_lastName, new_firstName, new_lastName, new_phone, new_email)
            print(f"Contact {old_firstName} {old_lastName} updated.")
        else:
            print(f"Contact {old_firstName} {old_lastName} not found.")

    
    def search_contact(self):

        type = input("What do you want to search by? Firstname, lastname or phone: ").lower()
        if type == "firstname":
            firstName = input("Enter the first name of the contact to search: ")
            contact = self.phonebook.search_contact_by_firstName(firstName)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print(f"Contact {firstName} not found.")
        
        elif type == "lastname":
            lastName = input("Enter the last name of the contact to search: ")
            contact = self.phonebook.search_contact_by_lastName(lastName)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print(f"Contact {lastName} not found.")
        
        elif type == "phone":
            phone = input("Enter the firstname of the contact to search: ")
            contact = self.phonebook.search_contact_by_phone(phone)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print(f"Contact {phone} not found.")
        
        elif type == "email":
            email = input("Enter the email of the contact to search: ")
            contact = self.phonebook.search_contact_by_email(email)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print(f"Contact {email} not found.")

        else:
            print(f"Option {type} not available. Please try again.")


    def display_contacts(self):
        print("Contacts: ")
        self.phonebook.display_contacts()


    def sort_contacts(self):

        type = input("Do you want to sort by firstname or lastname? ").lower()
        if type == "firstname":
            sort_type = input("Ascending or descending: ").lower()
            self.phonebook.sort_contacts_by_firstName(sort_type)
        elif type == "lastname":
            sort_type = input("Ascending or descending: ").lower()
            self.phonebook.search_contact_by_lastName(sort_type)

        else:
            print(f"Option {type} not available. Please try again.")
        
        print("Contacts sorted")


    def save_contacts(self):
        self.phonebook.save_contacts_to_file("Agenda.csv")
        print(f"Contacts saved to file.")

    
    def load_contacts(self):
        self.phonebook.load_contacts_from_file("Agenda.csv")
        print("Contacts loaded.")


    def undo_operation(self):
        self.phonebook.undo_operation()


    def run(self):

        running  = True
        while running:

            system("cls")
            self.display_menu()
            choice = int(input("Choose an option: "))

            if choice == 1:
                self.display_contacts()
                print("Press enter to continue")
                input()
            elif choice == 2:
                self.add_contact()
                print("Press enter to continue")
                input()
            elif choice == 3:
                self.delete_contact()
                print("Press enter to continue")
                input()
            elif choice == 4:
                self.edit_contact()
                print("Press enter to continue")
                input()
            elif choice == 5:
                self.search_contact()
                print("Press enter to continue")
                input()
            elif choice == 6:
                self.sort_contacts()
                print("Press enter to continue")
                input()
            elif choice == 7:
                self.save_contacts()
                print("Press enter to continue")
                input()
            elif choice == 8:
                self.load_contacts()
                print("Press enter to continue")
                input()
            elif choice == 9:
                quest = input("Are you sure you want to undo? Y/N: ").lower()
                if quest == "y":
                    self.undo_operation()
                    print("Press enter to continue")
                    input()
                elif quest == "n":
                    print("Press enter to continue")
                    input()
            elif choice == 10:
                if self.phonebook.dirty == True:
                    quest = input("You have unsaved changes. Are you sure you want to proceed? Y/N: ").lower()
                    if quest == "y":
                        running = False
                    elif quest == "n":
                        self.save_contacts()
                        print("Changes saved. Press enter to exit.")
                        input()
                        running = False
                elif self.phonebook.dirty == False:
                    running = False


agenda = Menu()
agenda.run()

