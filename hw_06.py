from collections import UserDict

class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone
                break

    def __str__(self):
        return str(self.name)

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record

    def delete_record(self, name):
        del self.data[name]

    def edit_record(self, old_name, new_name):
        record = self.data[old_name]
        record.name.value = new_name
        self.data[new_name] = record
        del self.data[old_name]

    def search_records(self, **criteria):
        results = []
        for record in self.data.values():
            match = True
            for key, value in criteria.items():
                if key == 'name':
                    if str(record.name) != value:
                        match = False
                        break
                elif key == 'phone':
                    if not any(str(phone) == value for phone in record.phones):
                        match = False
                        break
            if match:
                results.append(record)
        return results

def add_contact(command):
    _, name, phone = command.split()
    if name in contacts:
        return "Contact already exists."
    else:
        record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)
        return "Contact added."

def change_contact(command):
    _, name, phone = command.split()
    if name not in contacts:
        return "Contact not found."
    else:
        record = contacts.data[name]
        record.phones = []
        record.add_phone(phone)
        return "Contact updated."

def get_phone(command):
    _, name = command.split()
    if name in contacts:
        record = contacts.data[name]
        return ', '.join(str(phone) for phone in record.phones)
    else:
        return "Contact not found."

def show_all_contacts():
    if not contacts.data:
        return "No contacts found."
    else:
        return "\n".join(str(record) + ': ' + ', '.join(str(phone) for phone in record.phones) for record in contacts.data.values())

def user_command(command):
    command = command.lower()

    if command == "hello":
        return "How can I help you?"
    if command.startswith("add"):
        return add_contact(command)
    if command.startswith("change"):
        return change_contact(command)
    if command.startswith("phone"):
        return get_phone(command)
    if command == "show all":
        return show_all_contacts()
    if command in ["good bye", "close", "exit"]:
        return "Good bye!"
    return "Invalid command. Please try again."

def main():
    print("Welcome!")
    while True:
        command = input("Enter a command: ")
        result = user_command(command)
        print(result)
        if result == "Good bye!":
            break


if __name__ == "__main__":
    contacts = AddressBook()
    main()
