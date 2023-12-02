import pickle


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[phone] = name

    def save_to_book(self, file_address):
        with open(file_address, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_book(self, file_address):
        try:
            with open(file_address, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            print('File not found. Address book is empty.')

    def search_contact(self, query):
        result = {}
        for phone, name in self.contacts.items():
            if query.lower() in name.lower() or query in phone:
                result[phone] = name
        return result


address_book = AddressBook()
address_book.add_contact("Іван", "123456789")
address_book.add_contact("Петро", "987654321")
address_book.add_contact("Stepan", "00228899345987654321")
address_book.save_to_book("address_book.pkl")

# Завантаження з диска
new_address_book = AddressBook()
new_address_book.load_from_book("address_book.pkl")

# Пошук контакту
search_result = new_address_book.search_contact("00")
print("Результат пошуку:", search_result)
