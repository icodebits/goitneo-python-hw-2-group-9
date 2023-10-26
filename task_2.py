from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

    @staticmethod
    def is_valid_phone(value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if not isinstance(phone, Phone):
            phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p != phone]

    def edit_phone(self, old_phone, new_phone):
        new_phone = Phone(new_phone)
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value

    def __str__(self):
        phone_list = '; '.join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_list}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    if john:    # Перевірка запису до редагування
        john.edit_phone("1234567890", "1112223333")

    print(john) # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    if found_phone: # Перевірка запису до виведення
        print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555
    
    # Видалення запису Jane
    book.delete("Jane")
