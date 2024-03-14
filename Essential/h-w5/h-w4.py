# п.4 Використовуючи код з завдання 2, створити 2 екземпляри обох класів. Використати функції isinstance() –
# для перевірки екземплярів класу (за яким класом створені) та issubclass() – для перевірки і визначення класу-нащадка.

class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        pass

    def sent_message(self):
        pass


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        pass


contact1 = Contact("surname3", "name3", 20, 3803, "3@gmail.com")
up_contact1 = UpdateContact("surname1", "name1", 18, 3801, "1@gmail.com", "job1")
print(isinstance(contact1, Contact))
print(isinstance(up_contact1, Contact))
print(isinstance(up_contact1, UpdateContact))
print(issubclass(UpdateContact, Contact))
